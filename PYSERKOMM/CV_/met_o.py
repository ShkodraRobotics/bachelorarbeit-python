import serial
import Kommunik_class as kom
import serial.tools.list_ports



class me:
    global conn

    def __init__(self):
        pass
    def conect_tk(self,in_tex):
        global conn
        in_tex = int(in_tex)
        conn = kom.COM__(in_tex)
        return conn.con()

    def valu(c):
        conn.write(c)
    def list_insert(self):
        list.delete(0,"end")
        li_por = []
        ports = serial.tools.list_ports.comports()
        for i in ports:
            li_por.append(str(i))
        for i in li_por:
            list.insert('end',i)
        return None
    def sel(self):
        sell = list.curselection()
        for i in sell:
            it = list.get(i)
        print(it[3:4])
        num = it[3:4]
        print(num)
        self.conect_tk(num)

