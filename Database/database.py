import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
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
