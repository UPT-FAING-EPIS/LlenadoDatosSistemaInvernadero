import unittest
import numpy as np
from Model.splineModel import SplineModel

class TestSplineModel(unittest.TestCase):
    def setUp(self):
        self.time = np.array([0., 1., 2., 3., 4.])
        self.temperature = np.array([0., 1., 2., 3., 4.])
        self.model = SplineModel(self.time, self.temperature)

    def test_evaluate_spline(self):
        for t, temp in zip(self.time, self.temperature):
            result = self.model.evaluate_spline(t)
            self.assertAlmostEqual(result, temp, places=5)

    def test_find_temperature(self):
        for i in range(len(self.time)-1):
            t = (self.time[i] + self.time[i+1]) / 2 
            expected_temp = (self.temperature[i] + self.temperature[i+1]) / 2 
            result = self.model.find_temperature(t)
            self.assertAlmostEqual(result, expected_temp, places=5)

if __name__ == '__main__':
    unittest.main()
