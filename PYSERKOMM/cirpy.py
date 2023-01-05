import time
import serial
#co = input('COM?')
co = 8
ser = serial.Serial('COM' + str(co), 115200)  # open serial port


while True:
    command = input("Farbe :")
    """if command not 'r' or command not 'g' or command not 'b':
        ser.close()
        break"""
    com_l = len(command)
    com_l = str(com_l)
    command = command + ';'
    print(command)

    com = command.encode()
    ser.write(com)     # write a string



    b = ''
    a = ser.read()
    a = a.decode('utf-8')
    print(f'erstesa {a}')
    a = int(a)
    for i in range(a):
        a = ser.read()
        a = a.decode('utf-8')
        if a == ";":
            a = ''
            break

        else:
            b += a





    #a.replace('b','')
    #rint(a)
    print(b)
