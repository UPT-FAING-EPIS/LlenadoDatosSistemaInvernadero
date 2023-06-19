from behave import given, when, then
import numpy as np
from Model.splineModel import SplineModel

@given('time values and corresponding temperatures')
def step_given_time_and_temperatures(context):
    context.time = np.array([0., 1., 2., 3., 4.])
    context.temperature = np.array([0., 1., 2., 3., 4.])
    context.model = SplineModel(context.time, context.temperature)

@when('the spline is evaluated at these time points')
def step_evaluate_spline(context):
    context.results = [context.model.evaluate_spline(t) for t in context.time]

@then('all returned temperatures should be close to the provided temperatures')
def step_check_spline_evaluation(context):
    for result, temp in zip(context.results, context.temperature):
        assert abs(result - temp) < 0.00001

@when('the temperature is searched at specific time points')
def step_find_temperature(context):
    context.time_points = [(context.time[i] + context.time[i+1]) / 2 for i in range(len(context.time)-1)]
    context.expected_temps = [(context.temperature[i] + context.temperature[i+1]) / 2 for i in range(len(context.temperature)-1)]
    context.results = [context.model.find_temperature(t) for t in context.time_points]

@then('the returned temperatures should be close to the expected temperatures')
def step_check_found_temperatures(context):
    for result, expected_temp in zip(context.results, context.expected_temps):
        assert abs(result - expected_temp) < 0.00001
