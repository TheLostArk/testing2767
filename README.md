# testing2767

This Flask Service was created from the NerdWallet Flask Service boilerplate.

If this is your shiny new service, here are some things of interest to you...


## First steps

Run the following commands on your desktop:

1. Run `indy develop` to setup your virtual environment and install all Python dependencies.
1. Activate the virtualenv -- follow the instructions in the output of `indy develop`/`indy deps`.
1. Look in setup.py and ensure you have all the requirements you need.
1. Run `indy deps` to compile you full set of dependencies to requirements.txt.
1. Run `gu-dev-server` to run a local gunicorn development server

### Second steps

* Run `indy lint` to lint your project
* Run `indy test` to run your unit and integration tests, and also lint


## How Do I Develop My Service?

All of your applications code is located in the `src/testing2767` folder.  The rest of the paths in this
section will be relative to this folder.

### Builds & Versioning

Your service follows a master-only branch model.  This means that any commits that land in master will trigger a Jenkins
job to build an artifact of your service that can be deployed.  These Jenkins jobs are automatically configured based on
the existence of the Jenkinsfile in your project.

The version of your service is auto-incremented upon every successful build, so you do not need to worry about managing
the version yourself.

When you open a PR against your service the full build will run, but nothing will be published until the commit lands in
master.

### Flask Controllers

* Create a new module in `flask_app/controllers/`.  The module should register all routes against a module-level
  blueprint.
* Register the new controller's blueprint during app creation in `flask_app/__init__.py`
* Keep your controllers thin and push complicated functionality down to library and model code.

#### Customizing Flask server initialization

* Customize `flask_app/__init__.py`

### Library code

Add packages or modules to `lib/`

### Adding configuration

* After running `indy develop` you will have a `configs/` folder at the root of your project.  This is the app-configs
  repo, and contains configuration for all NerdWallet deployables.
* Create a new folder named `configs/deployables/testing2767`
* Inside that folder create a file named `default.yml` that contains any defaults.
* You can also add `dev.yml`, `test.yml`, `stage.yml`, and `prod.yml` files with environment specific configs.
* See https://github.com/NerdWallet/app-configs for more info.

### Adding or removing Python package dependencies

* Add or remove your dependency from `setup.py`
* If you aren't sure what versions are available, then run `indy pip install package_name==0`
* Run `indy deps`

### Testing

You can run `indy test` to run all tests inside of your project, including linting.  You can run `indy lint` if you
want to just run the linter.

Often times you'll want to just run `py.test` directly so that you can only run tests on a smaller subset.  In this
case you'll need to provide an environment variable so that your config loader will use the config from the test
environment (you'll also have to have run `indy test` once so that the test config is compiled):

```
CONFIG_NAME=config-testing.json py.test ...
```

Where `...` are the rest of your arguments to py.test.

See http://pytest.readthedocs.io/en/latest/ for more details on testing with pytest.


## How Do Setup My Database (if I want one)?

1. Create a setting in your `configs/deployables/testing2767/default.yml` file named `DATABASE_URI`.  Point
   this to whatever you'd like for development.  Some good choices for this setting are:
   `mysql+pymysql://root@localhost/testing2767` or `sqlite://testing2767.db`.  If in doubt ask in
   `#engineeringhelp` on Slack
1. Request Database access from devopshelp@
1. DevOps will add the DSNs to the configs for `stage.yml` & `prod.yml` when your access is provisioned.
1. Uncomment the database dependencies section of `setup.py` and run `indy deps`.
1. Uncomment the database configuration section and corresponding imports from `flask_app/__init__.py`.
1. To test out your fancy new database connection, write your first DB model and then uncomment the example DB query
   from `src/flask_app/controllers/health_check_controller.py`.

Don't want to have to explicitly call `g.session.commit()` on write endpoints?  Just update your Flask SQLAlchemy
instantation from `flask_app/__init.py` to `db = SQLAlchemy(app, session_options={'autocommit': True})`.

### Database migrations

* Run `alembic revision -m "What this revision does"` to create a database migration
* Run `alembic upgrade head` to migrate your database

All of these commands can be run on both your desktop and from within the localnerd VM.  When starting a new service
it is often most convenient to simply do all of your development on your desktop until you are ready to integrate with
other services inside of the VM.  Email devopshelp@ to have your service included in the nightly VM box build.


## How Do I Get My App Deployed?

1. Fill out a Requirements Doc: https://nerdwallet.atlassian.net/wiki/display/ENG/Requirements
1. Open a devopshelp@ ticket to get a port assigned and have your application defined in the Museum.


## What if this is a Hackathon project?

♥ Hackathon!

If you don't need to integrate with anything else then you can follow the steps in this doc to develop the new service
on your desktop machine and just start hacking!

If you need to integrate with other services then you can run from within localnerd by simply making sure that your new
service is located at `/srv/nerdwallet/testing2767`, then reloading your vagrant instance.  Once it's back up
you can following the First Steps section from within the VM.
