# Import MainController class from main_controller.py
from main_controller import MainController

# Define serial port settings
port = 'COM3'
baudrate = 9600

# Define database settings
host = 'localhost'
user = 'root'
password = ''
database = 'db_th'

# Define sleep time between readings
sleep_time = 3

# Create MainController object with specified settings
controller = MainController(port, baudrate, host, user, password, database, sleep_time)

# Run the program
controller.run()
