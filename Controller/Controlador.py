from Model.Datos import Datos
from Model.PolinomioInterpolante import PolinomioInterpolante

class Controlador:
    def __init__(self, datos, polinomio_interpolante):
        self.datos = datos
        self.polinomio_interpolante = polinomio_interpolante

    def leer_datos(self, fichero):
        self.datos.leer_datos(fichero)

    def procesar_datos(self, datos):
        self.datos.procesar_datos(datos)

    def obtener_datos(self, desde, hasta):
        return self.datos.obtener_datos(desde, hasta)

    def generar_predicciones(self, grado, rango):
        coeficientes = self.polinomio_interpolante.calcular_coeficientes(grado)
        predicciones = self.polinomio_interpolante.generar_predicciones(coeficientes, rango)
        return predicciones
