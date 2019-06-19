from setuptools import find_packages, setup


# List your dependencies here
# PIN EXACT VERSIONS, and only list things you directly depend on
#
# If you change anything in this list don't forget to run: indy deps
#
# If you need to know what versions are available run: indy pip install package_name==0
#
# If you're unsure about anything please tag @NerdWallet/RelEng on your PR
#
# If you are using a SQL database, add the follow dependencies:
# alembic, Flask-SQLAlchemy, SQLAlchemy
#
# If you are using Celery, add the follow dependency:
# nwpy-celery
#
# If you need redis for caching or Celery, add the following dependency:
# redis

install_requires = [
    'Flask==0.12.4',
    'nw-api==2.43.0',
    'nwpy-gunicorn==1.1.1',
]


# get our version from the auto-version managed file
with open('VERSION') as version_fd:
    version = version_fd.read().strip()

setup(
    name='testing2767',
    version=version,
    install_requires=install_requires,

    packages=find_packages('src'),
    package_dir={'': 'src'},

    # If you need to distribute non-Python (.py) files with your app you must list it here under package_data
    # See: https://docs.python.org/2/distutils/setupscript.html#installing-package-data
    # package_data={},

    entry_points={
        'pex': [
            # If you use alembic you'll need to uncomment this so that you get an alembic entry point that
            # Can be used for running migrations from the production .pex file
            # 'alembic = script',
        ],

        # to satisfy our deployable interface we install the control script from nwpy-deployable
        'console_scripts': [
            'control = nerdwallet.deployable.control:main',
        ],

        # specify which workers we want our control script to run
        'control_scripts': [
            'gunicorn = nerdwallet.gunicorn.deployable:control',
        ],

        # gunicorn needs to know where to find our app object
        'gunicorn': [
            'app = testing2767.flask_app:get_app'
        ],
    }
)
