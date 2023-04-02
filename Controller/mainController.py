from Model.splineModel import SplineModel
from View.splineView import SplineView

class SplineController:
    def __init__(self):
        self.view = SplineView(self)
        self.model = None

    def run(self):
        self.view.start()

    def find_roots(self, x_values, y_values, y_punto):
        self.model = SplineModel(x_values, y_values)
        return self.model.find_roots(y_punto)
