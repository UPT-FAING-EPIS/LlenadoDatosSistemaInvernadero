from Model.splineModel import SplineModel
from View.splineView import SplineView

class SplineController:
    def __init__(self):
        self.view = SplineView(self)
        self.model = None

    def run(self):
        self.view.start()

    def find_temperatures(self, time_values, temperature_values, time_points):
        self.model = SplineModel(time_values, temperature_values)
        return self.model.evaluate_spline(time_points)
