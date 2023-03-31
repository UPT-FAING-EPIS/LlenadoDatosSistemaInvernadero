from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

class Vista(QWidget):
    def __init__(self,controlador):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        # Etiqueta para mostrar el menú
        self.menu_label = QLabel("Seleccione una opción:", self)
        self.menu_label.move(10, 10)
        
        # Botones del menú
        self.leer_datos_button = QPushButton("Leer datos de archivo", self)
        self.leer_datos_button.move(10, 30)
        self.obtener_datos_button = QPushButton("Obtener datos de la base de datos", self)
        self.obtener_datos_button.move(10, 60)
        self.generar_predicciones_button = QPushButton("Generar predicciones", self)
        self.generar_predicciones_button.move(10, 90)
        
        # Etiquetas y campos de texto para solicitar información al usuario
        self.archivo_label = QLabel("Nombre del archivo:", self)
        self.archivo_label.move(10, 130)
        self.archivo_textbox = QLineEdit(self)
        self.archivo_textbox.move(120, 130)
        
        self.fechas_label = QLabel("Rango de fechas:", self)
        self.fechas_label.move(10, 160)
        self.desde_label = QLabel("Desde:", self)
        self.desde_label.move(120, 160)
        self.desde_textbox = QLineEdit(self)
        self.desde_textbox.move(170, 160)
        self.hasta_label = QLabel("Hasta:", self)
        self.hasta_label.move(120, 190)
        self.hasta_textbox = QLineEdit(self)
        self.hasta_textbox.move(170, 190)
        
        self.grado_label = QLabel("Grado del polinomio interpolante:", self)
        self.grado_label.move(10, 220)
        self.grado_textbox = QLineEdit(self)
        self.grado_textbox.move(230, 220)
        
        self.temperaturas_label = QLabel("Rango de temperaturas:", self)
        self.temperaturas_label.move(10, 250)
        self.temperatura_desde_label = QLabel("Desde:", self)
        self.temperatura_desde_label.move(120, 250)
        self.temperatura_desde_textbox = QLineEdit(self)
        self.temperatura_desde_textbox.move(170, 250)
        self.temperatura_hasta_label = QLabel("Hasta:", self)
        self.temperatura_hasta_label.move(120, 280)
        self.temperatura_hasta_textbox = QLineEdit(self)
        self.temperatura_hasta_textbox.move(170, 280)
        
        # Etiqueta para mostrar los datos obtenidos de la base de datos
        self.datos_label = QLabel(self)
        self.datos_label.move(10, 310)
        
        # Etiqueta para mostrar las predicciones generadas
        self.predicciones_label = QLabel(self)
        self.predicciones_label.move(10, 340)
        
        # Configuración de la ventana
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Sistema de Monitoreo y Control de Temperatura y Humedad Ambiental")
        self.show()
