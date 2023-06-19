Feature: Database
  The database should correctly insert and retrieve temperature data.

  Scenario: Insert and retrieve temperature
    Given a connection to the database
    When a temperature is inserted at a specific time point
    Then the same temperature should be retrieved when searched by that time point
