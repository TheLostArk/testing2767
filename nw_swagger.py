from testing2767.flask_app import get_app, open_api_generator

app = get_app()
with open('VERSION') as version_fd:
    version = version_fd.read().strip()

spec = open_api_generator.generate_spec('testing2767',
                                        description='testing2767',
                                        api_version=version)
