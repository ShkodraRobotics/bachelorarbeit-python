import pickle


class rec():

    def __init__(self):
        self.A1 = 0
        self.A2 = 0
        self.A3 = 0
        self.klaue = 0
        self.Base = 0
        self.aufnahme = []

    def aufn(self, x):
        self.aufnahme.append(x)

    def print(self):
        print(self.aufnahme)

    def speichern(self):
        A_liste = []
        B_liste = []
        C_liste = []
        D_liste = []
        E_liste = []
        for d in self.aufnahme:
            if d[0]=="A":
                A_liste.append(d)
            elif d[0]=="B":
                B_liste.append(d)
            elif d[0]=="C":
                C_liste.append(d)
            elif d[0]=="D":
                D_liste.append(d)
            elif d[0]=="E":
                E_liste.append(d)
        f = open("Record/recordings.txt", "w")
        for data in self.aufnahme:
            f.write(data)
            f.write(" ")
        #f.write(":")
        f.close()

    def offnen(self):
        file = open("Record/recordings.txt", "r")
        pre= ""
        list_f = []
        for f in file:
            pre+=f
        list = pre.split(" ")
        return list