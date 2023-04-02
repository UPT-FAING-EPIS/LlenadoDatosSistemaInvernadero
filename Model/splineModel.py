import numpy as np
from scipy.interpolate import splrep, splev
from scipy.optimize import bisect

class SplineModel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.spl = splrep(x, y)
    
    def evaluate_spline(self, x_new):
        return splev(x_new, self.spl)
    
    def find_roots(self, y_punto):
        # Función que devuelve la diferencia entre el valor del spline en un punto x y un valor y_punto dado
        def f(x, y_punto, spl):
            return splev(x, spl) - y_punto

        # Buscar los valores de x donde el spline es igual a y_punto
        raices = []
        for i in range(len(self.x)-1):
            a = self.x[i]
            b = self.x[i+1]
            if f(a, y_punto, self.spl)*f(b, y_punto, self.spl) < 0:  # Verificar si hay una raíz en el intervalo [a, b]
                raiz = bisect(f, a, b, args=(y_punto, self.spl))  # Buscar la raíz usando bisect
                raices.append(raiz)

        return raices
