import numpy as np
from scipy.interpolate import splrep, splev
from scipy.optimize import bisect

class SplineModel:
    def __init__(self, time, temperature):
        self.time = time
        self.temperature = temperature
        self.spl = splrep(time, temperature)
    
    def evaluate_spline(self, time_new):
        return splev(time_new, self.spl)
    
    def find_temperature(self, time_point):
        # Function that returns the difference between the value of the spline at a time point and a given temperature value
        def f(temperature, time_punto, spl):
            return splev(time_punto, spl) - temperature

        # Find the temperature at the given time point
        temperature = None
        for i in range(len(self.time)-1):
            a = self.time[i]
            b = self.time[i+1]
            if a <= time_point <= b:
                temperature = bisect(f, self.temperature[i], self.temperature[i+1], args=(time_point, self.spl))
                break

        return temperature

