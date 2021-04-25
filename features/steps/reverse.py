from behave import *
import json


@given('we have {input}')
def step_impl(context, input):
    context.input = json.loads(input)


@when('we reverse that data')
def step_impl(context):

    context.input = {value: key for key,
                     value in context.input.items()}


@then('it should look like {output}')
def step_impl(context, output):

    assert context.input == json.loads(output)
