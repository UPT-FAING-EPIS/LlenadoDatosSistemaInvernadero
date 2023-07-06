from behave import given, when, then
import numpy as np
from Controller.mainController import SplineController

@given('time values and temperature values')
def step_given_time_and_temperature_values(context):
    context.time_values = np.linspace(0, 2 * np.pi, 50)
    context.temperature_values = np.sin(context.time_values)
    context.time_points = np.linspace(0, 2 * np.pi, 100)

@when('the temperatures are calculated for the given time points')
def step_calculate_temperatures(context):
    controller = SplineController()
    context.result = controller.find_temperatures(context.time_values, context.temperature_values, context.time_points)

@then('all temperatures should be within the expected range')
def step_check_temperatures(context):
    tolerance = 0.0004

    min_allowed = context.temperature_values.min() - tolerance
    max_allowed = context.temperature_values.max() + tolerance

    assert np.all(min_allowed <= context.result) and np.all(context.result <= max_allowed)
