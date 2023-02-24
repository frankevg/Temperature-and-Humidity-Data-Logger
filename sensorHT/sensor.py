import serial

class Sensor:
    def __init__(self, port, baud_rate):
        self.port = port
        self.baud_rate = baud_rate

    def read_data(self):
        """Read data from the serial port and return the data as a dictionary."""
        try:
            with serial.Serial(self.port, self.baud_rate) as ard:
                data = ard.readline().decode("utf-8")
                humidity = float(data.split()[1])
                temperature = float(data.split()[4])
                heat_index = float(data.split()[11])
                return {
                    "humidity": humidity,
                    "temperature": temperature,
                    "heat_index": heat_index
                }
        except serial.SerialException as e:
            print(f"Error reading data from the sensor: {e}")
