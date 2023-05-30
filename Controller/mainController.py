from Model.splineModel import SplineModel


class SplineController:
    def __init__(self):
        self.model = None


    def find_temperatures(self, time_values, temperature_values, time_points):
        self.model = SplineModel(time_values, temperature_values)
        return self.model.evaluate_spline(time_points)
