"""Provide a factory function for generating new flask_app applications."""

from flask import Flask
# from flask import g
# from flask_sqlalchemy import SQLAlchemy

from nw_api import config as api_config
from nw_api.docgen.open_api.generator import OpenApiGenerator
from nw_api.logged_api import get_request_sensitive_params

from nerdwallet.app_config import config
from nerdwallet.logging import init_for_flask, override_log_levels
from nerdwallet.nwmonitor.bootstrap import bootstrap

from testing2767.flask_app import controllers

# Construct app.
app = Flask(__name__)
app.config.update(config.FLASK.OPTIONS)

# Configure loggers.
init_for_flask(app, extra_log_file=config.LOG_PATH, sentry_dsn=config.SENTRY_DSN,
               debug=config.DEBUG or config.IS_TEST_ENV,
               get_sentry_sensitive_parameters=get_request_sensitive_params,
               get_sentry_show_stacktrace_locals=lambda: True)

if not config.DEBUG:
    # quiet down chatty INFO loggers when we're not in DEBUG mode
    override_log_levels({
        'requests.packages.urllib3': 'WARN',
        'boto': 'WARN',
        'boto3': 'WARN',
        'botocore': 'WARN',
    })

# Configure database.
# app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
# app.config['SQLALCHEMY_POOL_RECYCLE'] = 235
# db = SQLAlchemy(app)

# @app.before_request
# def init_global_db_session():
#     g.session = db.session

# Register blueprints and OpenAPI docgen hooks.
api_modules = [
    controllers.example,
    controllers.health_check,
]
open_api_generator = OpenApiGenerator()
for m in api_modules:
    app.register_blueprint(m.blueprint)
    open_api_generator.add_api(m.api)

# Bootstrap monitoring
bootstrap()


def get_app():
    """Entry-point used to fetch the app object"""
    return app
