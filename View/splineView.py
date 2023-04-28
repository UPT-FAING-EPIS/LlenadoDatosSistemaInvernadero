from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from Model.splineModel import SplineModel

class SplineView:
    def __init__(self, controller):
        self.controller = controller

        # Crear ventana principal
        self.root = Tk()
        self.root.title("Spline Interpolation")

        # Crear frames
        main_frame = Frame(self.root, padx=20, pady=20)
        button_frame = Frame(self.root)

        # Crear y posicionar widgets
        Label(main_frame, text="Hora: ").grid(row=0, column=0, sticky=W)
        self.x_entry = Entry(main_frame)
        self.x_entry.grid(row=0, column=1)

        Label(main_frame, text="Temperatura: ").grid(row=1, column=0, sticky=W)
        self.y_entry = Entry(main_frame)
        self.y_entry.grid(row=1, column=1)

        Label(main_frame, text="Hora a revisar: ").grid(row=2, column=0, sticky=W)
        self.y_punto_entry = Entry(main_frame)
        self.y_punto_entry.grid(row=2, column=1)

        calculate_button = Button(button_frame, text="Calculate", command=self.calculate)
        calculate_button.pack(side=LEFT, padx=5)

        quit_button = Button(button_frame, text="Quit", command=self.root.destroy)
        quit_button.pack(side=LEFT, padx=5)

        # Posicionar frames
        main_frame.pack()
        button_frame.pack()

        # Crear label para mostrar resultados
        self.result_label = Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.start()

    def calculate(self):
        x_values = list(map(float, self.x_entry.get().split(",")))
        y_values = list(map(float, self.y_entry.get().split(",")))
        x_punto = float(self.y_punto_entry.get())

        # Llamar al método correspondiente en el controlador
        raices = self.controller.find_temperatures(x_values, y_values, x_punto)

        # Mostrar los resultados
        result_str = "Temperatura en la hora dada = {}: {}".format(x_punto, raices)
        self.result_label.config(text=result_str)

        # Graficar el spline
        self.plot_spline(x_values, y_values)

    def start(self):
        self.root.mainloop()

    def plot_spline(self, x_values, y_values):
        # Crear instancia de SplineModel y calcular el spline
        spline_model = SplineModel(x_values, y_values)
        spline_x = np.linspace(x_values[0], x_values[-1], num=1000)
        spline_y = spline_model.evaluate_spline(spline_x)

        # Crear figura y ejes
        fig, ax = plt.subplots()

        # Graficar el spline y los puntos
        ax.plot(spline_x, spline_y, label="Spline Interpolation")
        ax.scatter(x_values, y_values, label="Data Points")

        # Configurar leyenda, ejes y título
        ax.legend()
        ax.set_xlabel('Horas')
        ax.set_ylabel('Temperaturas')
        ax.set_title('Spline Interpolation')

        # Mostrar la gráfica
        plt.show()
