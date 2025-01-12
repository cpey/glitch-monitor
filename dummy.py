import serial

class Dummy:
    def __init__(self, serial_port, baudrate):
        self.serialport = serial_port
        self.baudrate = baudrate
        self.ser = serial.Serial(self.serialport, self.baudrate)
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

    @property
    def in_waiting(self):
        return self.ser.in_waiting

    def readline(self):
        try:
            line = self.ser.readline()
            return line.decode('utf-8').rstrip()
        except:
            return "Error"
