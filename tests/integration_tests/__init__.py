from nw_api.test import NWApiTestCase
# from mockredis import mock_redis_client

from testing2767.flask_app import app
# from models import session


class ControllerTestCase(NWApiTestCase):
    flask_app = app

    def setUp(self):
        # session.close()
        # session.remove()
        # from models import *  # NOQA
        # BaseModel.metadata.drop_all(engine)
        # BaseModel.metadata.create_all(engine)

        # redis
        # redis_patcher = mock.patch('redis.Redis', mock_redis_client)
        # redis_patcher.start()
        # self.addCleanup(redis_patcher.stop)

        # don't send email
        import nwutils
        nwutils.config.SEND_EMAILS = False

        # mock auth/csrf
        # mock_middleware('nw_api.csrf_protected_api.CsrfProtectionMiddleware', NullMiddleware())

        super(ControllerTestCase, self).setUp()
