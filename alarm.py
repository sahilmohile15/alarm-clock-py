#!/usr/bin/python

import os
import tkinter as tk
import datetime as dt
from playsound import playsound


#Creating Window and Label
window = tk.Tk()
title = tk.Label(text="Alarm Clock")
title.pack()


t1 = dt.time(hour=13,minute=15)
t2 = dt.time(hour=12,minute=54)
timetable = [t1, t2]


#Adding a button to stop time
sButton = tk.Button(
    text="Stop",
    bg = "blue",
    fg = "red",
    width = 15,
    height= 3,
)

sButton.pack()

window.mainloop()


while True:
    for i in timetable:
        if i.hour == dt.datetime.now().hour and i.minute == dt.datetime.now().minute:
            print("Its working...")
            break