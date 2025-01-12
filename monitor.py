#!/usr/bin/env python3
import serial

from controller import Controller
from dummy import Dummy

serial_port_dummy = '/dev/ttyUSB0'
serial_port_controller = '/dev/ttyACM0'
baudrate = 115200

correct_execution_result = "Expected execution"

def run():
    dummy = Dummy(serial_port_dummy, baudrate)
    controller = Controller(serial_port_controller, baudrate)

    resp = controller.set_delay(0)
    print(f"Controller response: {resp}")

    while True:
        controller.run_test_cycle()
        if dummy.in_waiting > 0:
            line = dummy.readline()
            print(f">>> {line}")
            if line != correct_execution_result and not line == "Error":
                import pdb; pdb.set_trace()
                print(f"Received from dummy: {line}")
                break

if __name__=="__main__":
    run()
