from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from Model.splineModel import SplineModel
class SplineView:
    def __init__(self, controller):
        self.controller = controller

        self.root = Tk()
        self.root.title("Spline Interpolation")

        # Labels y entry boxes para ingresar los datos de los puntos
        Label(self.root, text="X values: ").grid(row=0, column=0)
        self.x_entry = Entry(self.root)
        self.x_entry.grid(row=0, column=1)

        Label(self.root, text="Y values: ").grid(row=1, column=0)
        self.y_entry = Entry(self.root)
        self.y_entry.grid(row=1, column=1)

        # Entry box para ingresar el valor de y_punto
        Label(self.root, text="Y value to search: ").grid(row=2, column=0)
        self.y_punto_entry = Entry(self.root)
        self.y_punto_entry.grid(row=2, column=1)

        # Botón para calcular el spline y mostrar los resultados
        calculate_button = Button(self.root, text="Calculate", command=self.calculate)
        calculate_button.grid(row=3, column=0)

        self.result_label = Label(self.root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2)
        self.start()

    def calculate(self):
        x_values = list(map(float, self.x_entry.get().split(",")))
        y_values = list(map(float, self.y_entry.get().split(",")))
        y_punto = float(self.y_punto_entry.get())

        # Llamar al método correspondiente en el controlador
        raices = self.controller.find_roots(x_values, y_values, y_punto)

        # Mostrar los resultados
        result_str = "X values corresponding to y = {}: ".format(y_punto)
        result_str += ", ".join(str(x) for x in raices)
        self.result_label.config(text=result_str)
        self.plot_spline(x_values, y_values)

    def start(self):
        self.root.mainloop()
    def plot_spline(self, x_values, y_values):
        # Crear instancia de SplineModel y calcular el spline
        spline_model = SplineModel(x_values, y_values)
        spline_x = np.linspace(x_values[0], x_values[-1], num=1000)
        spline_y = spline_model.evaluate_spline(spline_x)

        # Graficar el spline
        plt.plot(spline_x, spline_y)
        plt.scatter(x_values, y_values)

        # Configurar los ejes y mostrar la gráfica
        plt.xlabel('X values')
        plt.ylabel('Y values')
        plt.title('Spline Interpolation')
        plt.show()
