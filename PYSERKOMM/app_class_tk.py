import time
import tkinter as tk
from tkinter import ttk
import serial
import Kommunik_class as kom
import serial.tools.list_ports
import opencv_stre
import cv2
from PIL import ImageTk, Image
import numpy as np
import Slider_ as sl
import Servo_KL as sr
import threading
import Aufnamhe_mod as am
global STATE
global cap
#Klasse erbt von tk.frame und ist für das vidoe da
class nootebook_frame(tk.Frame):
    global roboOB
    global th2



    def __init__(self):
        super().__init__()
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        STATE = False
        self.widget()

        self.status = 0
        self.rec = am.rec()
        self.roboOB = sr.Robo_arm()
        self.A1 = None
        self.A2 = None
        self.A3 = None
        self.Base = None
        self.KL = None


    def statusGeter(self):
        return self.status

    def statusSetter_ON(self):
        self.status = 1
    def statusSeter_OFF(self):
        self.status = 0

    def printer(self):
        self.rec.print()
        self.rec.speichern()
    def rec_auf(self):
        data = self.rec.offnen()
        for d in data:
            self.giver(d)
            #print(d)


    #global cap
    global STATE
    STATE = False
    @classmethod
    def ausgCaller(cls):
        posi = roboOB.ausgag()
        print(posi)
        for data in posi:
            nootebook_frame.giver(data)

    @classmethod
    def greifCaller(cls,po):
        posi = po
        print(posi)
        for data in posi:
            nootebook_frame.giver2(data)

    def status_ch(self):
        print(self.status)
        self.status = 1
        print(self.status)
    def giver(self,t):
        print(t)
        if t.startswith("A"):
            if t != self.Base:
                self.Base = t
                if self.statusGeter() == 1:
                    self.rec.aufn(t)
            k = t.strip("A")
            k = k.rstrip(";")
            #print("ich bin k " + k)
            self.roboOB.setBase(k)
        elif t.startswith("B"):
            if t != self.A3:
                self.A3 = t
                if self.statusGeter() == 1:
                    self.rec.aufn(t)
            k = t.strip("B")
            k = k.rstrip(";")
            #print(k)
            self.roboOB.setA3(k)
        elif t.startswith("C"):
            if t != self.A2:
                self.A2 = t
                if self.statusGeter() == 1:
                    self.rec.aufn(t)
            k = t.strip("C")
            k = k.rstrip(";")
            print(k)
            self.roboOB.setA2(k)
        elif t.startswith("D"):
            if t != self.A1:
                self.A1 = t
                if self.statusGeter() == 1:
                    self.rec.aufn(t)
            k = t.strip("D")
            k = k.rstrip(";")
            #print(k)
            self.roboOB.setA1(k)
        elif t.startswith("E"):
            if t != self.KL:
                self.KL = t
                if self.statusGeter() == 1:
                    self.rec.aufn(t)
            k = t.strip("E")
            k = k.rstrip(";")
            #print(k)
            self.roboOB.setKlaue(k)
        else:
            print("ERRROR beim senden unerwarteter wert")

        conn.write(t)

    @classmethod
    def giver2(cls, t):
        if nootebook_frame.statusGeter() == 1:
            self.rec.aufn(t)

        #conn.write(t)
        #print(t)

    def greif(t):

        roboOB.greif_posi(t)




    def widget(self):
#connest bekommt die nummer gesliced aus dem text
#global conn um zuzugreifen
#ein objekt non Comm die klasse verbindet metro mit laptop
        global th2

        def conect_tk(in_tex):
            global conn
            in_tex = int(in_tex)
            conn = kom.COM__(in_tex)

            #but3.config(state="disabled")

            return conn.con()
#hebt die verbindung auf funktioniert lösch aber objekt nicht
        def disc():

            kom.COM__.closer(conn)
            but3.config(state="active")

#erstellt eine liste aller com ports und insertet sie in die liste
        def list_insert():
            list.delete(0, "end")
            li_por = []
            ports = serial.tools.list_ports.comports()
            print(ports)
            for i in ports:
                li_por.append(str(i))
            for i in li_por:
                list.insert('end', i)
# Selection wird von button aufgerufen und bekommt was augewähltwurde damit der name complet in der liste angezeigt wird wird
# der slice verwendet user sieht vollen namen übergeben wird eine nummer an connect_tk
        def sel():
            sell = list.curselection()
            for i in sell:
                it = list.get(i)
            #print(it[3:4])
            num = it[3:4]
            #print(num)
            conect_tk(num)
        style = ttk.Style(self)
        style.configure('lefttab.TNotebook', tabposition='wn')
        def frame_():
            vid_num = video_source.get()
            int(vid_num)
            video(vid_num)
# hier wird die nummer eingegeen für die kammera die man beutzen will
# cap objekt die das video aufnimmt von der gewählten quelle cap als global um zugriff zu haben
# stream wird aufgerufen
        def video(num_sorce):
            try:
                global cap
                num_sorce = int(num_sorce)

                cap = cv2.VideoCapture(num_sorce)
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

                #global cap
                print('Video-Läuft')
                #th3 =threading.Thread(target=stream,daemon=True)
                #th3.start()
                stream()
            except ValueError:
                print('kein-Video')
        def stream_braker():
            global STATE
            cap = 0
            #cv2.VideoCapture.release()
            STATE = True
# um den stream aufzuhalten, funktioniert noch nicht richtig
        def stream_braker2():
            global STATE
            STATE = False
            frame_()
# cap wird eingelesen keine übergabe da global noch keine bearbeitung oder erkennung bild wird in tk bild umgewandelt
# um es ins canvas zu tun damit es im bild angezeigt wird
        def stream():

            while True:
                _,frame = cap.read()
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)
                image = ImageTk.PhotoImage(image)

                canvas.create_image(0,0, image = image,anchor = tk.NW)
                self.update()
                #time.sleep(0.2)
        def slider():

            pass

        def controller_loper(k):
            while STATE:
                k.con_loop()
        def Man_steuerung(x):
            global stop_event
            stop_event = threading.Event()
            STATE = True
            a1 = self.roboOB.A1
            a2 = self.roboOB.A2
            a3 = self.roboOB.A3
            base = self.roboOB.Base
            klaue = self.roboOB.Klaue
            import Controller
            Kontroller = Controller.Controller(base,a3,a2,a1,klaue)
            Kontroller.controller_cn()
            while True:

                data = Kontroller.con_loop()
                for d in data:
                    self.giver(d)
                if stop_event.is_set():
                    break
        def Man_steuerung_dek():
            exitflag1 = True
            th2 = threading.Thread(target=Man_steuerung, args =(lambda : exitflag1, ),daemon=True)
            th2.start()
        def man_dak():
            x = False
            #Man_steuerung_dek(x)
            stop_event.set()
        def slider0(i):
            str(i)

            ls0 = "A" + i + ";"
            #print(" ich bin im slider " + ls0)
            self.giver(ls0)
        def slider1(i):
            str(i)
            ls0 = "B" + i + ";"
            self.giver(ls0)
        def slider2(i):
            str(i)
            ls0 = "C" + i + ";"
            self.giver(ls0)
        def slider3(i):
            str(i)
            ls0 = "D" + i + ";"
            self.giver(ls0)
        def slider4(i):
            str(i)
            ls0 = "E" + i + ";"
            self.giver(ls0)

        #die buttons und slider
        notebook = ttk.Notebook(self,style='lefttab.TNotebook' )

        f1 = tk.Frame(notebook, width=2000, height=2000)
        f1.grid(sticky='nsew')
        slid0 = tk.Scale(f1, from_=0, to=180, orient=tk.HORIZONTAL, command=slider0, label= "Base")
        slid0.grid(row=1,column=1,sticky=tk.NW,)
        slid0.set(85)


        slid1 = tk.Scale(f1, from_=0, to=180, orient=tk.HORIZONTAL, command=slider1, label= "A3")
        slid1.grid(row=2, column=1, sticky=tk.NW, columnspan=2)
        slid1.set(100)

        slid2 = tk.Scale(f1, from_=0, to=180, orient=tk.HORIZONTAL, command=slider2, label= "A2")
        slid2.grid(row=3, column=1, sticky=tk.NW, columnspan=2)
        slid2.set(100)
        slid3 = tk.Scale(f1, from_=0, to=180, orient=tk.HORIZONTAL, command=slider3, label= "A1")
        slid3.grid(row=4, column=1, sticky=tk.NW, columnspan=2)
        slid3.set(12)
        slid4 = tk.Scale(f1, from_=0, to=180, orient=tk.HORIZONTAL, command=slider4, label= "Klaue")
        slid4.grid(row=5, column=1, sticky=tk.NW, columnspan=2,)
        slid4.set(0)



        slid5 = tk.Scale(f1, from_=180, to=0, orient=tk.VERTICAL, command=nootebook_frame.greif, label="Greifer")
        slid5.grid(row=5, column=2, sticky=tk.NW, columnspan=2)
        slid5.set(0)

        but2 = tk.Button(f1, command=list_insert, text='COM-PORT-Liste')
        but2.grid(row=7,column=1,sticky=tk.E)

        but3 = tk.Button(f1, command=sel, text='Connect!')
        but3.grid(row=7,column=1,sticky=tk.W)

        but4 = tk.Button(f1, command=disc, text='Discon!')
        but4.grid(row=7, column=2, sticky=tk.W)
        but5 = tk.Button(f1, command=nootebook_frame.ausgCaller, text='ausgang')
        but5.grid(row=7, column=3)
        list = tk.Listbox(f1)
        list.grid(row=6,column=1,sticky=tk.EW,columnspan=3)

        f2 = tk.Frame(notebook, width=2000, height=2000)

        lmain = tk.Label(f2)
        lmain.grid(column=0,row=0)

        video_source = tk.Entry(f2,)
        video_source.grid(column=0,row=2)


        but4 = tk.Button(f2, command=frame_, text='con')
        but4.grid(row=3, column=0)
        but5 = tk.Button(f2, command=stream_braker, text='Breaker')
        but5.grid(row=3, column=1)
        but6 = tk.Button(f2, command=stream_braker2, text='VIdeo')
        but6.grid(row=3, column=2)





        f3 = tk.Frame(notebook, width=2000, height=2000)
        f3.grid(sticky='nsew')

        but1_F3 = tk.Button(f3,command=Man_steuerung_dek, text='Kontroller')
        but1_F3.grid(row=0, column=0)
        but2_F3 = tk.Button(f3,command=man_dak, text='Kontroller-Deaktivieren')
        but2_F3.grid(row=1, column=0)
        but3_F3 = tk.Button(f3,command=self.statusSetter_ON, text='Aufnahme-aktiviere')
        but3_F3.grid(row=2, column=0)
        but4_F3 = tk.Button(f3,command=self.printer, text='Aufnahme-Speichern')
        but4_F3.grid(row=3, column=0)
        but5_F3 = tk.Button(f3,command=self.rec_auf, text='Aufnahme-Abspielen')
        but5_F3.grid(row=4, column=0)



        canvas = tk.Canvas(f2, width=640, height=480)
        canvas.grid(column=0,row=1)
        notebook.add(f1, text='Controll',)
        notebook.add(f2, text='Frame 2')
        notebook.add(f3, text='Manuell')
        notebook.grid(row=0, column=0, sticky="nw")
# klasse app die von tk erbt und von app-app aufgerufen wird
class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('RoBo-Vission')
        self.geometry('1300x640')
        self.resizable(True, True)
        self.widget()

    def widget(self):
        fram1 = nootebook_frame()
        fram1.grid(column = 0 , row = 0)


"""
if __name__ == '__main__':
    App = app()
    App.mainloop()
    
    """