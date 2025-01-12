import serial

class Controller:
    def __init__(self, serial_port, baudrate):
        self.serialport = serial_port
        self.baudrate = baudrate
        self.ser = serial.Serial(self.serialport, self.baudrate)

    def send_command(self, cmd, recv_response=False):
        response = ""
        self.ser.write(f"{cmd}\r".encode("utf-8"))
        if recv_response:
            response = self.ser.readline().decode('utf-8').rstrip()
        return response
        
    def set_delay(self, delay):
        cmd = f"s d {delay}"
        response = self.send_command(cmd, True)
        return response

    def set_ext_trigger(self, delay):
        cmd = f"s t {delay}"
        response = self.send_command(cmd)
        return response

    def power_off(self):
        cmd = f"s s 0"
        response = self.send_command(cmd)
        return response

    def power_on(self):
        cmd = f"s s 1"
        response = self.send_command(cmd)
        return response

    def run_delay(self):
        cmd = f"r d"
        response = self.send_command(cmd)
        return response

    def run_test_cycle(self):
        self.power_off()
        self.power_on()
        response = self.run_delay()
        print(response)
        return response

