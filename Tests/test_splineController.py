import unittest
from Controller.mainController import SplineController
import numpy as np

class TestSplineController(unittest.TestCase):
    def setUp(self):
        self.controller = SplineController()

    def test_find_temperatures(self):
        time_values = np.linspace(0, 2 * np.pi, 50)
        temperature_values = np.sin(time_values)
        time_points = np.linspace(0, 2 * np.pi, 100)
        result = self.controller.find_temperatures(time_values, temperature_values, time_points)

        tolerance = 0.0004

        min_allowed = temperature_values.min() - tolerance
        max_allowed = temperature_values.max() + tolerance

        self.assertTrue(np.all(min_allowed <= result) and np.all(result <= max_allowed))


if __name__ == '__main__':
    unittest.main()
