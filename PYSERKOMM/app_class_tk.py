import tkinter as tk
from tkinter import ttk
import serial
import Kommunik_class as kom
import serial.tools.list_ports
import opencv_stre
import cv2
from PIL import ImageTk, Image
import numpy as np

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

    def widget(self):
        def conect_tk(in_tex):
            global conn
            in_tex = int(in_tex)
            conn = kom.COM__(in_tex)
            return conn.con()

        def valu(c):
            conn.write(c)

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











        notebook = ttk.Notebook(self,style='lefttab.TNotebook' )

        f1 = tk.Frame(notebook, width=200000, height=2000)
        f1.grid(sticky='nsew')
        slid = tk.Scale(f1, from_=0, to=100, orient=tk.HORIZONTAL, command=valu)
        slid.grid(row=0,column=1,sticky=tk.NW,columnspan=2)

        but2 = tk.Button(f1, command=list_insert, text='COM-PORT-Liste')
        but2.grid(row=3,column=1,sticky=tk.E)

        but3 = tk.Button(f1, command=sel, text='Connect!')
        but3.grid(row=3,column=1,sticky=tk.W)

        list = tk.Listbox(f1)
        list.grid(row=2,column=1,sticky=tk.EW)

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














