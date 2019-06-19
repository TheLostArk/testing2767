""" canonical objects are used to serialize and de-serialize data in nw_api. You can convert
instances of your models to canonicals to return them as JSON from your APIs, or use canonicals
to validate and parse JSON into your APIs """

from nw_api import validate


class Example(validate.Validator):
    id = validate.StringType()
    created_at = validate.DateTimeType()
    title = validate.StringType()

    @classmethod
    def from_model(cls, model):
        return cls({
            'id': model.id,
            'created_at': model.created_at,
            'title': model.title,
        })
