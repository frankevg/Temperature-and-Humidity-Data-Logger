import mysql.connector
import datetime

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        """Connect to the database and return the connection object."""
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return self.conn
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL database: {e}")

    def insert_data(self, humidity, temperature, heat_index):
        """Insert humidity, temperature, and heat index data into the database."""
        try:
            cursor = self.conn.cursor()
            sql = "INSERT INTO th (humedad, temperatura, indice_calor, fecha) VALUES (%s, %s, %s, %s)"
            now = datetime.datetime.now()
            val = (humidity, temperature, heat_index, now)
            cursor.execute(sql, val)
            self.conn.commit()
            cursor.close()
            print(cursor.rowcount, "record inserted.")
            
        except mysql.connector.Error as e:
            print(f"Error inserting data: {e}")

    def disconnect(self):
        """Close the database connection."""
        self.conn.close()
