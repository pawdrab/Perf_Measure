import random
import tkinter as tk
import serial
from time import *
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import os


diffT = 0
diffV = 0
kmh = 0
gps = serial.Serial("com6", baudrate=9600)
pomiarTrwa = False
def clear_terminal():
    os.system('cls')



#pomiar od x do y
zacznijPomiarV = 10
zakończPomiarV = 100

x = 1 + zacznijPomiarV
y = 0.5 + zakończPomiarV


while True:

    clear_terminal()
    ser_bytes = gps.readline()
    decoded_bytes = ser_bytes.decode("latin")
    data = decoded_bytes.split(",")

    if data[0] =="$GNRMC":
        knots = data[7]
        knots_changed = float(knots)
        seconds = float(data[1])
        kmh1 = round(knots_changed * 1.852, 2)       
        kmh = kmh1 + kmh

        print(str(seconds) + "    " + str(pomiarTrwa) + "   " + str(kmh))

        if pomiarTrwa == False and kmh < x:
            print("Gotowy do pomiaru")

        if not pomiarTrwa and kmh > x:
            startT = seconds
            startV = kmh
            pomiarTrwa = True     
            print()       
            print("Zaczyna sie pomiar "+ str(startT) + " " + str(startV))
        elif kmh<1:
            pomiarTrwa = False

        if kmh >= y:
            endT = seconds
            endV = kmh
            print()
            print("Zakończono pomiar")
            print("Czas: " + str(zacznijPomiarV) + "-" + str(zakończPomiarV) + " = " + str(round(endT - startT,2)) + " s")
            print("StartV: " + str(round(startV,2)) + " endV: " + str(round(endV,2)))
            break

        #print("Prędkość:  " + str(round(kmh,2)) + " km/h  "+ str(data[1]))
        with open("Chip234.txt", "a", encoding="UTF-8") as file:
            file.write("\n"  + " | " + str(data[1]) + " | " + str(round(kmh,2)))
#
#
# root.mainloop()