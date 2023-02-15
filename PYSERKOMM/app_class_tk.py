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




global STATE
global cap

class nootebook_frame(tk.Frame):

    def __init__(self,cont):
        super().__init__(cont)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        STATE = False
        self.widget()





    #global cap
    global STATE
    STATE = False



    def giver(t):

        conn.write(t)

    def widget(self):

        def conect_tk(in_tex):
            global conn
            in_tex = int(in_tex)
            conn = kom.COM__(in_tex)

            but3.config(state="disabled")

            return conn.con()

        def disc():

            conn.close()
            but4.config(state="active")


        def list_insert():
            list.delete(0, "end")
            li_por = []
            ports = serial.tools.list_ports.comports()
            print(ports)
            for i in ports:
                li_por.append(str(i))
            for i in li_por:
                list.insert('end', i)

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

        def stream_braker2():
            global STATE
            STATE = False
            frame_()


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









        notebook = ttk.Notebook(self,style='lefttab.TNotebook' )

        f1 = tk.Frame(notebook, width=2000, height=2000)
        f1.grid(sticky='nsew')
        slid0 = tk.Scale(f1, from_=0, to=180, orient=tk.HORIZONTAL, command=sl.slid_me.slider0, label= "Base",resolution=10)
        slid0.grid(row=0,column=1,sticky=tk.NW,)
        slid0.set(85)

        slid1 = tk.Scale(f1, from_=0, to=180, orient=tk.HORIZONTAL, command=sl.slid_me.slider1, label= "A3")
        slid1.grid(row=1, column=1, sticky=tk.NW, columnspan=2)
        slid1.set(100)

        slid2 = tk.Scale(f1, from_=0, to=180, orient=tk.HORIZONTAL, command=sl.slid_me.slider2, label= "A2")
        slid2.grid(row=3, column=1, sticky=tk.NW, columnspan=2)
        slid2.set(100)
        slid3 = tk.Scale(f1, from_=0, to=180, orient=tk.HORIZONTAL, command=sl.slid_me.slider3, label= "A1")
        slid3.grid(row=4, column=1, sticky=tk.NW, columnspan=2)
        slid3.set(12)
        slid4 = tk.Scale(f1, from_=0, to=180, orient=tk.HORIZONTAL, command=sl.slid_me.slider4, label= "Klaue")
        slid4.grid(row=5, column=1, sticky=tk.NW, columnspan=2)
        slid4.set(0)

        but2 = tk.Button(f1, command=list_insert, text='COM-PORT-Liste')
        but2.grid(row=7,column=1,sticky=tk.E)

        but3 = tk.Button(f1, command=sel, text='Connect!')
        but3.grid(row=7,column=1,sticky=tk.W)

        but4 = tk.Button(f1, command=disc, text='Discon!')
        but4.grid(row=7, column=2, sticky=tk.W)

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
        canvas = tk.Canvas(f2, width=640, height=480)
        canvas.grid(column=0,row=1)
        notebook.add(f1, text='Controll',)
        notebook.add(f2, text='Frame 2')
        notebook.grid(row=0, column=0, sticky="nw")

class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('RoBo-Vission')
        self.geometry('1600x840')
        self.resizable(True, True)

        self.widget()
    def widget(self):
        fram1 = nootebook_frame(self)
        fram1.grid(column = 0 , row = 0)














