import mysql.connector
from datetime import datetime

class Datos:
    def __init__(self, archivo, db_host, db_user, db_password, db_name):
        self.archivo = archivo
        self.db_host = db_host
        self.db_user = db_user
        self.db_password = db_password
        self.db_name = db_name
    
    def leer_datos(self):
        # Leer datos del archivo
        datos = []
        with open(self.archivo, 'r') as f:
            for linea in f:
                valores = linea.strip().split(',')
                temperatura = float(valores[0])
                humedad = float(valores[1])
                horario = datetime.strptime(valores[2], '%Y-%m-%d %H:%M:%S')
                datos.append((temperatura, humedad, horario))
        return datos
    
    def guardar_datos(self, datos):
        # Guardar datos en la base de datos MySQL
        cnx = mysql.connector.connect(host=self.db_host, user=self.db_user, password=self.db_password, database=self.db_name)
        cursor = cnx.cursor()
        insert_query = ("INSERT INTO mediciones "
                        "(temperatura, humedad, horario) "
                        "VALUES (%s, %s, %s)")
        for medicion in datos:
            cursor.execute(insert_query, medicion)
        cnx.commit()
        cursor.close()
        cnx.close()
