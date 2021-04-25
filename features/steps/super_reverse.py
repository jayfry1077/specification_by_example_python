from behave import *
from src.main import super_json_reverser
import json


@given('{input_data} for our super_json_reverser')
def step_impl(context, input_data):
    context.input_data = json.loads(input_data)


@when('we call our super_json_reverser function')
def step_impl(context):

    context.input_data = super_json_reverser(context.input_data)


@then('we should get the following {output_data}')
def step_impl(context, output_data):

    assert context.input_data == json.loads(output_data)
