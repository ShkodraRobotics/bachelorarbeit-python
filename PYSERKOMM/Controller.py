import hid
import serial
import time
from Kommunik_class import COM__
import serial
import Servo_KL



class Controller():




    def __init__(self,base, A3, A2, A1,kl,gre):
        self.id = 0x3285
        self.pr_id = 0x0c03
        self.gamepad = None
        self.gpad_coder = { 1 : "Y", 2 : "B" ,4:"A",8:"X", 32: "R1", 128 : "R2", 64:"L2" ,16 :"L1"
        }

        self.cn = serial.Serial("COM9",115200)
        self.base = base
        self.A3 = A3
        self.A2 = A2
        self.A1 = A1
        self.kl = kl
        self.gr = gre
        self.cn.flush()
        self.mover=4


    def print(self,data):
        print(data[3])
        print(data[2])
        for d in data:
            self.write2(d)
            #print(d)

    def write2(self, data):
        try:
            data = str(data)
            data = data.encode()
            self.cn.write(data)
        except:
            print("ERror_beim_senden")

    def controller_cn(self):

        try:

            self.gamepad = hid.Device(self.id, self.pr_id)
            self.gamepad.nonblocking

        except OSError as e:
            print(e)


    def dec(self,rep):
        #Analog-Stick

        ba = rep[3]
        if ba > 128:
            self.base += self.mover
        elif ba < 128:
            self.base -= self.mover
        if self.base > 180:
            self.base = 180
        elif self.base < 0:
            self.base = 0
        basis = "A" +str(self.base) + ";"
        a3 = rep[4]
        if a3 > 128:
            self.A3 += self.mover
        elif a3 < 128:
            self.A3 -= self.mover
        if self.A3 > 180:
            self.A3 = 180
        elif self.A3 < 0:
            self.A3 = 0
        A3 = "B" + str(self.A3) + ";"

        #tasten
        a2a = rep[0]
        if a2a==4:
            self.A2+=self.mover
        if self.A2 >180:
            self.A2 = 180
        a2b= rep[0]
        if a2b==2:
            self.A2-=self.mover
        if self.A2 <0:
            self.A2 = 0
        A2 = "C" + str(self.A2) + ";"

        a1a = rep[0]
        if a1a==8:
            self.A1+=self.mover
        if self.A1 >180:
            self.A1 = 180
        a1b =rep[0]
        if a1b==1:
            self.A1 -= self.mover
        if self.A1 < 0:
            self.A1 = 0
        A1 = "D" + str(self.A1) + ";"

        greifer = rep[6]
        if greifer != 128:
            if greifer > 128:
                self.gr += self.mover
            elif greifer < 128:
                self.gr -= self.mover
            if self.gr > 180:
                self.gr = 180
            elif self.gr < 0:
                self.gr = 0

            A1,A2,self.A1,self.A2 = Servo_KL.Rob.cls_greif_posi(self.gr, self.A2, self.A1)


        dec_rep = [basis,A3,A2,A1]


        self.print(dec_rep)

















        #num3 = (num3 * 2/ 255) -1






        """ 
       if num3>0 :
            num3= 1- num3
        elif num3<0:
            num3 = 1 + num3
        else:
            num3 = 0

        num3/=10


        if num2 > 128:
            time.sleep(num3)
            self.cnt+=1
        elif num2 < 128:
            time.sleep(num3)
            self.cnt-=1

        if self.cnt >180:
            self.cnt =180
        elif self.cnt < 0:
            self.cnt = 0

        self.write2(f"E{self.cnt};")


        """

        """
        try:
            print(self.gpad_coder[num])
        except KeyError as e:
            print(e)
        """







    def con_loop(self):
        while True:
            report = self.gamepad.read(10)
            self.dec(report)
            #print([report[0]])





