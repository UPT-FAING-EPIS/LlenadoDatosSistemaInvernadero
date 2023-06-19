import mysql.connector

class Database:
    def __init__(self, host, user, password, database,port):
        self.connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )

    def insert_temperature(self, time_point, temperature):
        cursor = self.connection.cursor()
        query = "INSERT INTO temperatura (hora, temperatura) VALUES (%s, %s)"
        values = (time_point, temperature)
        cursor.execute(query, values)
        self.connection.commit()
    def get_temperature(self, time_point):
        cursor = self.connection.cursor()
        query = "SELECT temperatura FROM temperatura WHERE hora = %s"
        values = (time_point, )
        cursor.execute(query, values)
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None 
