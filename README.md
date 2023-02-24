# Temperature-and-Humidity-Data-Logger
The Temperature and Humidity Data Logger is a Python-based program that logs temperature and humidity data from a DHT11 sensor and stores it in a MySQL database. The program is designed to run on a pc connected via serial (COM port) to an Arduino with a DHT11 sensor.

The program uses two main controllers: main_controller.py and serial_controller.py. The main_controller.py file is responsible for initializing the serial and database controllers and running the program. The serial_controller.py file handles the communication with the DHT11 sensor over serial communication. The database_controller.py file is responsible for connecting to and interacting with the MySQL database.  The program continuously reads temperature and humidity data from the DHT11 sensor and stores it in the database. It also calculates the heat index based on the temperature and humidity readings. The data is stored in the database with a timestamp.  Installation and Usage To use the program, follow these steps:  Clone the repository. Install the required Python libraries: pyserial and mysql-connector-python. 

# Create a MySQL database and a table with the following schema:  sql 

  * CREATE TABLE db_th (
  * id INT NOT NULL AUTO_INCREMENT,
  * humidity INT NOT NULL,
  * temperature INT NOT NULL,
  * heat_index FLOAT NOT NULL,
  * timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  * PRIMARY KEY (id)); 

# Install the mysql-connector-python-rf library

$ pip install mysql-connector-python-rf

# Install the pySerial library

$ pip install pyserial

# Edit the main.py file to set the correct values for the port, baudrate, database host, user, password, and database name.  

Import MainController class from main_controller.py
* from main_controller import MainController

Define serial port settings
* port = 'COM3'
* baudrate = 9600

Define database settings
* host = 'localhost'
* user = 'root'
* password = ''
* database = 'db_th'

Define sleep time between readings
* sleep_time = 3

Create MainController object with specified settings
* controller = MainController(port, baudrate, host, user, password, database, sleep_time)

Run the program
* controller.run()

Run the main.py file: python main.py.  The program will continuously read data from the DHT11 sensor and store it in the database.
License The program is open source and is released under the MIT License. Feel free to use, modify, and distribute the program as you see fit.
