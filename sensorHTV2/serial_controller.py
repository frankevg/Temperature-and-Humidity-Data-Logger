# serial_controller.py
import serial #Import the PySerial library, which provides a way to communicate with serial port

class SerialController:
    def __init__(self, port, baudrate=9600):
        # Initializes the SerialController class with port and baudrate
        self.port = port
        self.baudrate = baudrate
        self.ser = None

    def open_serial(self):
        # Opens the serial connection with the specified port and baudrate
        self.ser = serial.Serial(self.port, self.baudrate)
        # Returns True if the connection is open, False otherwise
        return self.ser.is_open

    def close_serial(self):
        # Closes the serial connection
        self.ser.close()

    def read_data(self):
        # Reads data from the serial connection
        datos = self.ser.readline()
        datos_decode = datos.decode('utf-8')
        words = datos_decode.split()
        # Extracts humidity, temperature, and heat index data from the string
        humidity_str = words[1]
        temperature_str = words[4]
        heat_index_str = words[11]
        try:
            # Converts the extracted data to the appropriate data types
            humidity = int(float(humidity_str))
            temperature = int(float(temperature_str))
            heat_index = float(heat_index_str)
            return humidity, temperature, heat_index
        except ValueError:
            # Returns None for all values if the data cannot be converted
            return None, None, None
