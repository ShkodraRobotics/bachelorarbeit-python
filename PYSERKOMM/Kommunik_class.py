import serial
import time


class COM__:
    ser2 = None

    def __init__(self,port):
        self.port = port
        self.ser = None
    def con(self):
        self.ser = serial.Serial('COM' + str(self.port), 115200)  # open serial port
        #self.ser = serial.Serial('COM9', 115200)  # open serial port
        ser2 = serial.Serial('COM' + str(self.port), 115200)  # open serial port
        self.ser.flush()
       
        return ser2


    def write(self,data):
        try:
            data = str(data)
            print(data)
            data = data.encode()
            self.ser.write(data)
        except:
            print("Error_beim_senden")
    @classmethod
    def write2(cls, data, instanz):
        try:
            data = str(data)
            print(data)
            data = data.encode()
            instanz.ser.write(data)
        except:
            print("Error_beim_senden")

    def closer(self):
        self.ser.close()


