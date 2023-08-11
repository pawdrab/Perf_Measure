Miejsce zajęte w 81% … Możesz zwolnić miejsce lub uzyskać więcej miejsca na Dysku, w Gmailu i Zdjęciach Google.
import random
import tkinter as tk
import serial
from time import *
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
#
#
# root = tk.Tk()
# displayWidth = root.winfo_screenwidth()
# displayHeight = root.winfo_screenheight()
# root.config(bg="#000000")
# root.attributes("-fullscreen", True)
# root.geometry(str(displayWidth) + "x" + str(displayHeight) + "+0+0")
# pixel = tk.PhotoImage(width=1, height=1)
#
# buttonWidth = int(displayWidth / 3)
# buttonHeight = int(displayHeight / 4)
# paddingx = int(displayWidth / 20)
# paddingy = int(displayHeight / 20)
# fontSize = 25
#
# print("displayWidth = " + str(displayWidth) + " displayHeight = " + str(displayHeight))
# print("buttonWidth = " + str(buttonWidth) + " buttonHeight = " + str(buttonHeight))
# print("paddingx = " + str(paddingx) + " paddingy = " + str(paddingy))
#
# var = StringVar()
# var.set("Urządzenie gotowe do pomiaru")
# startButtonString = StringVar()
# startButtonString.set("Kliknij tutaj, aby zaczac pomiar")
#
# speed = 0
# speedTable = []
# timeTable = []

gps = serial.Serial("com6", baudrate=9600)

# def graph():
#     plt.plot(timeTable, speedTable)
#     plt.grid(visible=True)
#     plt.autoscale(enable=True, tight=True)
#     plt.locator_params(axis="both", tight=True, nbins=10)
#     plt.show()
#     print(round(float(timeTable[-1]), 2))
#
#
# def displayCurrentSpeed(speed):
#     var.set("V = " + str(round(speed, 2)) + " km/h")
#
#
# def displayCurrendTime(currentTime):
#     startButtonString.set("T = " + str(round(currentTime, 2)) + " s")
#     root.update_idletasks()
#
#
# def getStartSpeed():
#     startSpeed = startMeasurementSlider.get()
#     print("Start speed = " + str(startSpeed))
#     return startSpeed
#
#
# def getEndSpeed():
#     endSpeed = endMeasurementSlider.get()
#     print("End speed = " + str(endSpeed))
#     return endSpeed
#
#
# def myButton2Clicked():
#     graph()
#
# def myButton3Clicked():
#     root.destroy()
#
#
# def myButton1Clicked():
#     var.set("Oczekiwanie na przekroczenie V startowej")
#     root.update_idletasks()
#     measurement_time = measure(speed)
#     print(speedTable)
#     print(timeTable)
#     print("zarejestrowano " + str(len(speedTable)) + " próbek")
#     print("Czas = " + str(measurement_time))
#
#
# def measure(speed):
#     startSpeed = getStartSpeed()
#     endSpeed = getEndSpeed()
#     speedTable.clear()
#     timeTable.clear()
#     measurement_start = round(time(), 3)
#     while (speed < endSpeed):
#         addedValue = random.randint(1, 100) / 100
#         sleep(1 / 18)
#         speed = speed + addedValue
#         speedTable.append(round(speed, 3))
#         timeTable.append((round((time() - measurement_start), 3)))
#         x = ((speed - startSpeed) / (endSpeed - startSpeed)) * 100
#         displayCurrentSpeed(speed)
#         displayCurrendTime((time() - measurement_start))
#         speedProgressBar['value'] = x
#     measurement_stop = round(time(), 3)
#     startButtonString.set("Czas pomiaru : " + str(round((measurement_stop - measurement_start), 3)) + " s")
#     root.update_idletasks()
#     return (round((measurement_stop - measurement_start), 3))
#
#
# quitButton = Button(root, text="Wyjście", bg="#888888", command=myButton3Clicked, image=pixel, height=buttonHeight / 3,
#                     width=buttonWidth / 3, compound="c", font=("Arial", fontSize))
# quitButton.place(x=0, y=0)
#
# startButton = Button(root, textvariable=str(startButtonString), bg="#888888", command=myButton1Clicked, image=pixel,
#                      height=buttonHeight, width=buttonWidth, compound="c", font=("Arial", fontSize))
# startButton.place(x=paddingx, y=(displayHeight - buttonHeight - paddingy))
#
# showDiagramButton = Button(root, text="Pokaż wykres", bg="#888888", command=myButton2Clicked, image=pixel, height=buttonHeight / 3,
#                            width=buttonWidth/3, compound="c", font=("Arial", fontSize))
# showDiagramButton.place(x=displayWidth - buttonWidth/3, y=0)
#
# timeDisplayLabel = Label(root, textvariable=str(var), bg="#888888", image=pixel, height=buttonHeight, width=buttonWidth,
#                          compound="c", font=("Arial", fontSize))
# timeDisplayLabel.place(x=displayWidth - buttonWidth - paddingx, y=displayHeight - buttonHeight - paddingy)
#
# startMeasurementSlider = Scale(root, from_=0, label="V start", to=250, orient=HORIZONTAL, length=buttonWidth,
#                                width=buttonWidth / 5, sliderlength=buttonWidth / 5, font=("Arial", 50))
# startMeasurementSlider.place(x=paddingx, y=(displayHeight - buttonHeight) / 2)
#
# endMeasurementSlider = Scale(root, from_=0, label="V end", to=250, orient=HORIZONTAL, length=buttonWidth,
#                              width=buttonWidth / 5, sliderlength=buttonWidth / 5, font=("Arial", 50))
# endMeasurementSlider.place(x=displayWidth - buttonWidth - paddingx, y=(displayHeight - buttonHeight) / 2)
#
# speedProgressBar = ttk.Progressbar(root, orient=HORIZONTAL, length=displayWidth-2*paddingx, mode='determinate')
# speedProgressBar.place(x=paddingx, y=((displayHeight - buttonHeight) - ((displayHeight - buttonHeight) / 8)))

while True:
#
    ser_bytes = gps.readline()
    decoded_bytes = ser_bytes.decode("latin")
    data = decoded_bytes.split(",")
    # if data[0] == "$GNGGA":
    #     print("Liczba satelit w użyciu : " + str(data[7]))
    #     print("Metrów nad poziomem morza : " + str(data[9]) + " mnpm")

    if data[0] =="$GNRMC":
        knots = data[7]
        knots_changed = float(knots)
        kmh = round(knots_changed * 1.852, 2)
        print("Prędkość:  " + str(round(kmh,2)) + " km/h"+ str(data[1]))
        with open("Chip234.txt", "a", encoding="UTF-8") as file:
            file.write("\n" + str(round(kmh,2)) + "|" + str(data[1]))
#
#
# root.mainloop()