Feature: Spline Model
  The Spline Model should correctly calculate temperatures based on provided time points.

  Scenario: Evaluate Spline
    Given time values and corresponding temperatures
    When the spline is evaluated at these time points
    Then all returned temperatures should be close to the provided temperatures

  Scenario: Find temperature
    Given time values and corresponding temperatures
    When the temperature is searched at specific time points
    Then the returned temperatures should be close to the expected temperatures
