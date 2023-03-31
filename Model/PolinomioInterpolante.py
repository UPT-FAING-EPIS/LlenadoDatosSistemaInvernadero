import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

class PolinomioInterpolante:
    def __init__(self, temperatura, humedad):
        self.temperatura = temperatura
        self.humedad = humedad
        self.coeficientes = None

    def calcular_coeficientes(self, grado):
        X = np.array(self.temperatura).reshape(-1, 1)
        y = np.array(self.humedad).reshape(-1, 1)

        poly = PolynomialFeatures(degree=grado)
        X_poly = poly.fit_transform(X)

        lin_reg = LinearRegression()
        lin_reg.fit(X_poly, y)

        self.coeficientes = lin_reg.coef_[0][1:]

    def generar_predicciones(self, rango):
        if self.coeficientes is None:
            print("Error: se deben calcular los coeficientes primero.")
            return None

        X_pred = np.array(rango).reshape(-1, 1)
        poly_pred = PolynomialFeatures(degree=len(self.coeficientes))
        X_pred_poly = poly_pred.fit_transform(X_pred)

        y_pred = X_pred_poly @ self.coeficientes.reshape(-1, 1)
        return y_pred.flatten()
