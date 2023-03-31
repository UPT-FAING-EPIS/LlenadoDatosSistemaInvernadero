from Model.Datos import Datos
from Model.PolinomioInterpolante import PolinomioInterpolante
from Controller.Controlador import Controlador
from View.viewWinMain import Vista
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    # Inicializar la aplicación de PyQt5
    app = QApplication([])

    # Instanciar las clases del modelo
    datos = Datos(archivo='', db_host='localhost', db_user='root', db_password='', db_name='mediciones')
    interpolante = PolinomioInterpolante(13, 13)

    # Instanciar la clase del controlador
    controlador = Controlador(datos, interpolante)

    # Instanciar la clase de la vista
    vista = Vista(controlador)

    # Mostrar la vista
    vista.initUI()

    # Ejecutar la aplicación de PyQt5
    app.exec_()
