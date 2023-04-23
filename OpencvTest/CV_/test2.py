import serial

class kon:



        def __init__(self):
                self.port = "COM9"
                self.baud = 115200
                self.ser = None
        def con(self):
                self.ser = serial.Serial(self.port,self.baud)

        def writter(self,x):
                x = x.encode()
                self.ser.write(x)





