import pytest
from pytest_bdd import given, when, then, scenario

from tests.MongoObjects import MongoObjects


@scenario('morning.features', 'edit a profile')
def test_we_want_to_edit_profile_in_mongo_application():
    """edit profile"""
    pass


@pytest.fixture(scope='function')
def context():
    return {}


@given("there exist a profile")
def step_impl(context):
    context['objects'] = MongoObjects()


@when("I edit the profile")
def step_impl(context):
    context['objects'].edit_name("shimon")
    context['objects'].edit_mail("shimon@mail")
    context['objects'].edit_interests("music")
    context['objects'].update()


@then("the profile is actually edited")
def step_impl(context):
    mongo_name = context['objects'].get_mongo_name()
    mongo_mail = context['objects'].get_mongo_mail()
    mongo_interests = context['objects'].get_mongo_interests()
    context['objects'].close_drivers()
    assert(mongo_name == 'shimon')
    assert(mongo_mail == 'shimon@mail')
    assert(mongo_interests == 'music')
