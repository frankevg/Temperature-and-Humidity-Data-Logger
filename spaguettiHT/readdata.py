import serial
import time

import datetime
import mysql.connector

# Open the serial port
with serial.Serial('COM3', 9600) as ard:
    while True:
        # Read data from the serial port
        datos = ard.readline()
        datos_decode = datos.decode('utf-8')
        
        # Split the data into words
        words = datos_decode.split()
        humidity_str = words[1]
        temperature_str = words[4]
        heat_index_str = words[11]
        
        try:
            # Convert the data to the appropriate data type
            humidity = int(float(humidity_str))
            temperature = int(float(temperature_str))
            heat_index = float(heat_index_str)

            # Print the data
            print(humidity)
            print(temperature)
            print(heat_index)


            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_th"
            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO th (humedad,temperatura,indice_calor,fecha) VALUES (%s,%s,%s,%s)"
            now = datetime.datetime.now()
            val = (humidity,temperature,heat_index,now)

            mycursor.execute(sql, val)
            mydb.commit()

            print(mycursor.rowcount, "record inserted.")


        except ValueError:
            print("Error: Cannot convert to float")
        
        # Wait for a few seconds before reading data again
        time.sleep(3)
