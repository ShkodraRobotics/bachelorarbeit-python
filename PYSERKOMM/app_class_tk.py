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





global STATE
global cap
#Klasse erbt von tk.frame und ist für das vidoe da
class nootebook_frame(tk.Frame):
    global roboOB
    global th2
    roboOB = sr.Robo_arm()

    def __init__(self,cont):
        super().__init__(cont)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        STATE = False
        self.widget()
        sl.slid_me.objektTaker(roboOB)


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



    @classmethod
    def giver(cls,t):

        if t.startswith("A"):
            k = t.strip("A")
            k = k.rstrip(";")
            print(k)
            roboOB.setBase(k)
        elif t.startswith("B"):
            k = t.strip("B")
            k = k.rstrip(";")
            print(k)
            roboOB.setA3(k)
        elif t.startswith("C"):
            k = t.strip("C")
            k = k.rstrip(";")
            print(k)
            roboOB.setA2(k)
        elif t.startswith("D"):
            k = t.strip("D")
            k = k.rstrip(";")
            print(k)
            roboOB.setA1(k)
        elif t.startswith("E"):
            k = t.strip("E")
            k = k.rstrip(";")
            print(k)
            roboOB.setKlaue(k)
        else:
            print("ERRROR bei seten unerwarteter wert")

        conn.write(t)

    @classmethod
    def giver2(cls, t):
        conn.write(t)
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
            _,frame = cap.read()
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)

            canvas.create_image(0,0, image = image,anchor = tk.NW)
            self.update()

            if STATE == False:
                canvas.after(10,stream())
            else:
                pass

        def slider():

            pass

        def controller_loper(k):
            while STATE:
                k.con_loop()

        def Man_steuerung(x):
            global stop_event
            stop_event = threading.Event()
            STATE = True
            a1 = roboOB.A1
            a2 = roboOB.A2
            a3 = roboOB.A3
            base = roboOB.Base
            klaue = roboOB.Klaue
            import Controller
            Kontroller = Controller.Controller(base,a3,a2,a1,klaue)
            Kontroller.controller_cn()
            while True:

                Kontroller.con_loop()
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
















        #die buttons und slider
        notebook = ttk.Notebook(self,style='lefttab.TNotebook' )

        f1 = tk.Frame(notebook, width=2000, height=2000)
        f1.grid(sticky='nsew')
        slid0 = tk.Scale(f1, from_=0, to=180, orient=tk.HORIZONTAL, command=sl.slid_me.slider0, label= "Base")
        slid0.grid(row=1,column=1,sticky=tk.NW,)
        slid0.set(85)


        slid1 = tk.Scale(f1, from_=0, to=180, orient=tk.HORIZONTAL, command=sl.slid_me.slider1, label= "A3")
        slid1.grid(row=2, column=1, sticky=tk.NW, columnspan=2)
        slid1.set(100)

        slid2 = tk.Scale(f1, from_=0, to=180, orient=tk.HORIZONTAL, command=sl.slid_me.slider2, label= "A2")
        slid2.grid(row=3, column=1, sticky=tk.NW, columnspan=2)
        slid2.set(100)
        slid3 = tk.Scale(f1, from_=0, to=180, orient=tk.HORIZONTAL, command=sl.slid_me.slider3, label= "A1")
        slid3.grid(row=4, column=1, sticky=tk.NW, columnspan=2)
        slid3.set(12)
        slid4 = tk.Scale(f1, from_=0, to=180, orient=tk.HORIZONTAL, command=sl.slid_me.slider4, label= "Klaue")
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
        list.grid(row=6,column=1,sticky=tk.EW,columnspan=2)

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
        fram1 = nootebook_frame(self)
        fram1.grid(column = 0 , row = 0)



if __name__ == '__main__':
    App = app()
    App.mainloop()