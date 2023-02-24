import time
from sensor import Sensor
from database import Database

SENSOR_PORT = "COM3"
SENSOR_BAUD_RATE = 9600
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "db_th"


def main():
    # Create instances of the sensor and database classes
    sensor = Sensor(SENSOR_PORT, SENSOR_BAUD_RATE)
    db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    # Connect to the database
    db.connect()

    # Read data from the sensor, insert it into the database, and repeat
    while True:
        data = sensor.read_data()
        humidity = data["humidity"]
        temperature = data["temperature"]
        heat_index = data["heat_index"]
        db.insert_data(humidity, temperature, heat_index)
        time.sleep(3)

    # Disconnect from the database when the program ends
    db.disconnect()


if __name__ == "__main__":
    main()
