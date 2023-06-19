from behave import given, when, then
from Database.database import Database
from unittest.mock import patch, Mock

@given('a connection to the database')
def step_given_database_connection(context):
    context.mock_db = Mock()

    with patch('mysql.connector.connect', return_value=context.mock_db):
        context.db = Database('host', 'user', 'password', 'database', 'port')

    context.mock_cursor = Mock()
    context.mock_db.cursor.return_value = context.mock_cursor

@when('a temperature is inserted at a specific time point')
def step_insert_temperature(context):
    context.time_point = '12:00'
    context.temperature = 25.0
    context.db.insert_temperature(context.time_point, context.temperature)

@then('the same temperature should be retrieved when searched by that time point')
def step_retrieve_temperature(context):
    context.mock_cursor.fetchone.return_value = [context.temperature]
    result = context.db.get_temperature(context.time_point)
    assert result == context.temperature
