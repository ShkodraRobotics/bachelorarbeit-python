import serial
import time


class COM__:
    def __init__(self,port):
        self.port = port
        self.ser = None
    def con(self):
        self.ser = serial.Serial('COM' + str(self.port), 115200)  # open serial port
    def write(self,data):
        try:
            data = str(data)
            data = data.encode()
            self.ser.write(data)
        except:
            print("ERror_beim_senden")

    def closer(self):
        self.ser.close()


