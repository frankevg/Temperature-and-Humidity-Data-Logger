import datetime  # import the datetime module for getting the current date and time
import mysql.connector  # import the mysql.connector module for interacting with MySQL databases


class DatabaseController:
    def __init__(self, host, user, password, database):
        """
        Constructor method that initializes the instance variables for the host, user, password, and database.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.db = None  # create a variable for storing the database connection
        self.cursor = None  # create a variable for storing the cursor for executing SQL queries

    def connect_db(self):
        """
        Method for connecting to the MySQL database using the host, user, password, and database specified in the constructor.
        """
        self.db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.db.cursor()  # create a cursor for executing SQL queries on the database

    def insert_data(self, humidity, temperature, heat_index):
        """
        Method for inserting data into the 'th' table of the connected database.
        """
        sql = "INSERT INTO th (humedad, temperatura, indice_calor, fecha) VALUES (%s, %s, %s, %s)"  # SQL query for inserting data into the table
        now = datetime.datetime.now()  # get the current date and time
        val = (humidity, temperature, heat_index, now)  # create a tuple containing the data to be inserted
        self.cursor.execute(sql, val)  # execute the SQL query with the data tuple
        self.db.commit()  # commit the changes to the database
        return self.cursor.rowcount  # return the number of rows affected by the query

    def close_db(self):
        """
        Method for closing the database connection and cursor.
        """
        self.cursor.close()  # close the cursor
        self.db.close()  # close the database connection
