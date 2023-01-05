import time
import serial
import tkinterXcustom as tk
import Kommunik_class as kom
import serial.tools.list_ports



#inpu = input('COM?')



#co = 8
#ser = serial.Serial('COM' + str(co), 115200)  # open serial port


def conect_tk(in_tex):
    global conn
    in_tex = int(in_tex)
    conn = kom.COM__(in_tex)
    return conn.con()

def valu(c):
    conn.write(c)


def list_insert():
    list.delete(0,"end")
    li_por = []
    ports = serial.tools.list_ports.comports()
    for i in ports:
        li_por.append(str(i))
    for i in li_por:
        list.insert('end',i)
def sel():
    sell = list.curselection()
    for i in sell:
        it = list.get(i)
    print(it[3:4])
    num = it[3:4]
    print(num)
    conect_tk(num)



root = tk.Tk()

slid = tk.Scale(root, from_=0,to=100, orient=tk.HORIZONTAL,command=valu)
slid.pack()
"""
but = tk.Button(root,command=conect_tk,text='Com-Port')
but.pack()
entry = tk.Entry(root)
entry.pack()
"""
but2 = tk.Button(root,command=list_insert,text='list_insert' )
but2.pack()
but3 = tk.Button(root,command=sel,text='con')
but3.pack()
list = tk.Listbox(root,)
list.pack()



root.mainloop()










