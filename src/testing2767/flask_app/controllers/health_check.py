"""Provide basic health check endpoints for ELBs and monitoring."""
from flask import Blueprint

from nw_api.api import NWApi

# from functools import partial

# from testing2767.celery_app import tasks

from nwutils import nwlogging
from nwutils.health_check import HealthCheck

log = nwlogging.getNWLogger(__name__)

blueprint = Blueprint('health_check', __name__)
api = NWApi(blueprint, namespace='api', min_version=1, max_version=1,
            summary='Provide basic health check endpoints for ELBs and monitoring.')


@api.route('/health_check/', method='GET', require_caller=False, lookup_identity=False, skip_logging=True)
def health_check(_):
    """This is to be used by server side load balancers (ELB/ALB) for determining if we should be placed in service.

    This should be as simple and light weight as possible and only be used to determine if the application can serve
    requests.  Aspects such as the database being able to serve queries is better handled by the smoke_test, below.
    The reason for this is that even if some third-party system you rely on is down shouldn't impact this service.  We
    should code defensively enough in our implementations such that we may throw errors, but not for EVERY user.  We
    would rather serve some 200s and lots of 500s, than nothing but 503s.
    """
    return ''


@api.route('/smoke_test/', method='GET', require_caller=False, lookup_identity=False, skip_logging=True)
def smoke_test(_):
    """This is to be used by humans or an external monitoring status for the purpose of sending pages/notifications.

    For example, this should be hooked up to datadog and then trigger slack and/or pager duty warnings for the word
    'degraded' and alerts for the word 'unhealthy'.

    This should be hit no more than once per minute.
    """
    checks = HealthCheck()
    # checks.add_degraded('celery', partial(tasks.health_check.apply_async, safe=True))
    # checks.add_degraded('identity', check_url(api_config.IDENTITY_BASE_URL))
    # checks.add_unhealthy('database', partial(MyModel.query.first))
    return checks.get_response()


@api.route('/exception_test/', method='GET', require_caller=False, lookup_identity=False, skip_logging=True)
def exception_test(_):
    """This is to be used by humans for the purpose of checking alerting on uncaught errors.

    This should not be exposed via the edge; it is an internal-only endpoint.
    """
    raise Exception('Test Exception')
