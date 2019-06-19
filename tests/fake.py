""" this module is for creating fake records for your tests """
from uuid import uuid4


def create_example(**kwargs):
    defaults = dict(
        id=uuid4(),
        title='foobar',
    )
    defaults.update(kwargs)
    # return ExampleModel(**defaults).save()
    return None
