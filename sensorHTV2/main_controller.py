# Import necessary libraries
import time
from datetime import datetime
from serial_controller import SerialController
from database_controller import DatabaseController

# Define MainController class
class MainController:
    # Initialize class with port, baudrate, host, user, password, database, and sleep_time
    def __init__(self, port, baudrate, host, user, password, database, sleep_time):
        self.serial_controller = SerialController(port, baudrate)
        self.database_controller = DatabaseController(host, user, password, database)
        self.sleep_time = sleep_time

    # Define run method to run the program
    def run(self):
        # Attempt to open serial port
        if not self.serial_controller.open_serial():
            print("Error: Failed to open serial port")
            return

        # Connect to database
        self.database_controller.connect_db()

        # Enter infinite loop to continuously read and insert data
        while True:
            # Read humidity, temperature, and heat index data from serial port
            humidity, temperature, heat_index = self.serial_controller.read_data()

            # If all data is available, insert into database
            if humidity is not None and temperature is not None and heat_index is not None:
                count = self.database_controller.insert_data(humidity, temperature, heat_index)
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Humedad: {humidity}%, Temperatura: {temperature}°C, Indice de calor: {heat_index}°C")
                print( f"{now} -> ",count, "record(s) inserted")

            # Sleep for specified time before repeating loop
            time.sleep(self.sleep_time)

        # Close database and serial port connections when loop is exited
        self.database_controller.close_db()
        self.serial_controller.close_serial()