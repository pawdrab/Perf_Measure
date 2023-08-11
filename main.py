import random
import tkinter as tk
import serial
from time import *
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import os

#########################################################################
#
zacznijPomiarV = 0

zakończPomiarV = 100
#
#########################################################################

kmh = 0
gps = serial.Serial("com6", baudrate=9600)
pomiarTrwa = False
x = 1 + zacznijPomiarV
y = 0.5 + zakończPomiarV

def clear_terminal():
    os.system('cls')


while True:

    clear_terminal()
    ser_bytes = gps.readline()
    decoded_bytes = ser_bytes.decode("latin")
    data = decoded_bytes.split(",")

    if data[0] =="$GNRMC":
        knots = data[7]
        knots_changed = float(knots)
        seconds = float(data[1])
        kmh = round(knots_changed * 1.852, 2)       
        #kmh = round(kmh1 + kmh,2)#debug only
        print(str(seconds) + " | " + str(pomiarTrwa) + " | " + str(kmh) + " kmh")

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
            clear_terminal()
            print("Zakończono pomiar \n" )
            print("Start V: " + str(round(startV,2)) + " end V: " + str(round(endV,2)) + "\n")
            print("Czas " + str(zacznijPomiarV) + "-" + str(zakończPomiarV) + " = " + str(round(endT - startT,2)) + " s\n")
            break

        with open("Chip234.txt", "a", encoding="UTF-8") as file:
            file.write("\n"  + " | " + str(data[1]) + " | " + str(round(kmh,2)))