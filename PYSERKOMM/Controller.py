import hid
import serial
import time
from Kommunik_class import COM__
import serial
import Servo_KL
#from Servo_KL import Rob
import app_class_tk as ap
class Controller:

    def __init__(self, base, A3, A2, A1, kl):
        self.id = 0x3285
        self.pr_id = 0x0c03
        self.gamepad = None
        self.gpad_coder = {1: "Y", 2: "B", 4: "A", 8: "X", 32: "R1", 128: "R2", 64: "L2", 16: "L1"}
        #self.cn = serial.Serial("COM9", 115200)
        self.base = base
        self.A3 = A3
        self.A2 = A2
        self.A1 = A1
        self.kl = kl
        self.gr = 0
        #self.cn.flush()
        self.mover = 4

    def print(self, data):
        for d in data:
            self.write2(d)

    def write2(self, data):
        try:
            data = str(data)
            data = data.encode()
            ap.nootebook_frame.giver2(data)
        except:
            print("ERror_beim_senden")

    def controller_cn(self):
        try:

            self.gamepad = hid.Device(self.id, self.pr_id)
            self.gamepad.nonblocking

        except OSError as e:
            print(e)

    def dec(self, rep):
        # Analog-Stick
        #______LINKER ANALOG____LINKS_RECHTS______________
        ba = rep[3]
        if ba > 128:
            skale = ba
            skale = ((ba - 128) / 127) * 10
            print(ba)
            print(self.skal(127-ba+127))
            self.base -= int(self.skal(ba))
        elif ba < 128:
            print(self.skal(127 - ba + 127))
            skale2 = ((((ba / 127) * 10) - 10) * (-1))
            self.base += int(self.skal(127-ba+127))
        if self.base > 180:
            self.base = 180
        elif self.base < 0:
            self.base = 0
        basis = "A" + str(self.base) + ";"
        #____________LINKER___ANALOG____HOCH__RUNTER____
        a3 = rep[4]
        if a3 > 128:
            skale3 = ((a3 - 128) / 127) * 10
            self.A3 -= int(self.skal(a3))
        elif a3 < 128:
            skale4 = ((((a3 / 127) * 10) - 10) * (-1))
            self.A3 += int(self.skal(127-a3+127))
        if self.A3 > 180:
            self.A3 = 180
        elif self.A3 < 0:
            self.A3 = 0
        A3 = "B" + str(self.A3) + ";"

        # tasten
        #TASTE_B_A2__HOCH
        a2a = rep[0]
        if a2a == 4:
            self.gr = 0
            self.A2 += self.mover
        if self.A2 > 180:
            self.A2 = 180
        #TASTE__A__A2__RUNTER
        a2b = rep[0]
        if a2b == 2:
            self.gr = 0
            self.A2 -= self.mover
        if self.A2 < 0:
            self.A2 = 0
        A2 = "C" + str(self.A2) + ";"

        #TASTE__X__HOCH
        a1a = rep[0]
        if a1a == 8:
            self.A1 += self.mover
            self.gr = 0
        if self.A1 > 180:
            self.A1 = 180
        #TASTE__Y__RUNTER
        a1b = rep[0]
        if a1b == 1:
            self.A1 -= self.mover
            self.gr = 0
        if self.A1 < 0:
            self.A1 = 0
        A1 = "D" + str(self.A1) + ";"

        klaue = rep[0]
        if klaue == 128:
            self.kl += self.mover
        if self.kl > 180:
            self.kl = 180
        # TASTE__Y__RUNTER
        klaueb = rep[0]
        if klaueb == 64:
            self.kl -= self.mover
        if self.kl < 0:
            self.kl = 0
        kl = "E" + str(self.kl) + ";"





        #GREIFEN__SERVO__A1__A2__RECHTER__ANALOG__HOCHRUNTER
        greifer = rep[6]
        if greifer != 128:
            if greifer > 128:
                self.gr -= int(self.skal(greifer))
            elif greifer < 128:
                self.gr += int(self.skal(127-greifer+127))
            if self.gr > 180:
                self.gr = 180
            elif self.gr < -180:
                self.gr = -180
            print("posi" + str(self.gr))
            A1, A2, self.A1, self.A2 = Servo_KL.Rob.cls_greif_posi(self.gr, self.A2, self.A1)

        dec_rep = [A1, A2, A3, basis,kl]

        # time.sleep(2)
        self.print(dec_rep)

    def skal(self, x):
        if x > 240:
            s = 10
        elif 240 > x > 230:
            s = 6
        elif 230 > x > 200:
            s = 5
        elif 200 > x > 180:
            s = 4
        elif 180 > x > 160:
            s = 3
        elif 160 > x > 140:
            s = 2
        elif 140 > x > 128:
            s = 1
        else:
            s = 0
        return s

    def con_loop(self):

        report = self.gamepad.read(10)
        self.dec(report)
        # print([report[0]])
