from flask import Blueprint

from acls.scopes import identity as identity_scopes
from nw_api.api import NWApi

from testing2767.lib.canonical_objects import Example
# from testing2767.models.example import ExampleModel

blueprint = Blueprint('examples', __name__)
api = NWApi(blueprint, namespace='api', min_version=1, max_version=1,
            summary='Example')


@api.route('/examples',
           require_identity=True,
           require_one_of_scopes=(identity_scopes.GLOBAL_PROFILE_READ_ALL,))
def get_examples(_):
    models = []
    # models = ExampleModel.query.all()
    return Example.from_models(models)
