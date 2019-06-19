from acls.scopes import identity as identity_scopes

from testing2767.flask_app.controllers import example

from tests.integration_tests import ControllerTestCase


class ExampleTests(ControllerTestCase):
    nw_api = example.api

    def test_get_all(self):
        self.authenticate_as(scopes=(identity_scopes.GLOBAL_PROFILE_READ_ALL,))
        response = self.get('/examples')

        assert response.status_code == 200
        assert response.json_data is not None
