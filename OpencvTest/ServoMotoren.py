import Kommunikation as ko
import app_class_tk as a


class Robo_arm:

    def __init__(self):
        self.servo_min = 0
        self.servo_max = 180
        self.Klaue = 0
        self.Base = 180
        self.A1 = 0
        self.A2 = 0
        self.A3 = 0

    def setKlaue(self, klaue):
        self.Klaue = int(klaue)
        print(self.Klaue)

    def setBase(self, base):
        self.Base = int(base)

    def setA1(self, a1):
        self.A1 = int(a1)

    def setA2(self, a2):
        self.A2 = int(a2)

    def setA3(self, a3):
        self.A3 = int(a3)

    def ausgag(self):
        base = 'A0;'
        klaue = 'E50;'
        a1 = 'D180;'
        a2 = 'C20;'
        a3 = 'B100;'

        aus_li = [base, klaue, a1, a2, a3]

        return aus_li

    def greif_posi(self, pos):
        greif_posA2 = int(self.A2) + int(pos)
        greif_posA1 = int(self.A1) - int(pos)
        if greif_posA1 < 0:
            greif_posA1 = 0
        elif greif_posA1 > 180:
            greif_posA1 = 180

        if greif_posA2 < 0:
            greif_posA2 = 0
        elif greif_posA2 > 180:
            greif_posA2 = 180
        greif_posA1 = str(greif_posA1)
        greif_posA2 = str(greif_posA2)

        greif_posA1 = "D" + greif_posA1 + ";"
        greif_posA2 = "C" + greif_posA2 + ";"

        greifen = [greif_posA1, greif_posA2]
        print("ich bin Posittion" + pos)
        print("ich bin self a1" + self.A1)
        print("ich bin self a2" + self.A2)
        print(greifen)
        if int(self.A3) >= 70:
            greif_posA3 = int(self.A3) + int(pos)
            if greif_posA3 < 0:
                greif_posA3 = 0
            elif greif_posA3 > 180:
                greif_posA3 = 180
            greif_posA3 = str(greif_posA3)
            greif_posA3 = "B" + greif_posA3 + ";"
            greifen.append(greif_posA3)

        a.nootebook_frame.greifCaller(greifen)

    def safe_mod(self, posi):
        pass


class Rob:
    @staticmethod
    def cls_greif_posi(pos, A2, A1):
        pos/=180
        greif_posA2 = int(A2) + int(pos)
        greif_posA1 = int(A1) - int(pos)
        if greif_posA1 < 0:
            greif_posA1 = 0
        elif greif_posA1 > 180:
            greif_posA1 = 180

        if greif_posA2 < 0:
            greif_posA2 = 0
        elif greif_posA2 > 180:
            greif_posA2 = 180
        help_A1 = greif_posA1
        help_A2 = greif_posA2
        greif_posA1 = str(greif_posA1)
        greif_posA2 = str(greif_posA2)

        greif_posA1 = "D" + greif_posA1 + ";"
        greif_posA2 = "C" + greif_posA2 + ";"

        return greif_posA1, greif_posA2, help_A1, help_A2

