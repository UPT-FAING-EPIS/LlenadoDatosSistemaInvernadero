Feature: Spline Controller
  The spline controller should correctly find the temperatures given time values and temperature values.

  Scenario: Find temperatures
    Given time values and temperature values
    When the temperatures are calculated for the given time points
    Then all temperatures should be within the expected range
