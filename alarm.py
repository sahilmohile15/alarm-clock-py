#!/usr/bin/python

import os
import sys
import tkinter as tk
import datetime as dt
from playsound import playsound

'''
#Creating Window and Label
window = tk.Tk()
title = tk.Label(text="Alarm Clock")
title.pack()
'''

t1 = dt.time(hour=14,minute=39)
t2 = dt.time(hour=14,minute=43)
timetable = [t1, t2]
'''

#Adding a button to stop time
sButton = tk.Button(
    text="Stop",
    bg = "blue",
    fg = "red",
    width = 15,
    height= 3,
    command = stop
)

sButton.pack()

#Function to stop execution of code
def stop():
    exit()
'''
#def alarm():
for elt in timetable:
    i_time = elt
    #i_minute = i.minute
    while True:
        if i_time <= dt.datetime.now().time():
        #if i_hour == dt.datetime.now().hour and i_minute == dt.datetime.now().minute:
            #current_time = tk.Label(text = dt.datetime.now())
            #current_time.pack()
            #playsound('media/ClassAlarm.mp3')
            print("Its time")
            break



window.mainloop()


'''
for elt in timetable:
  time = dt.datetime.now().time()
  if time - elt < 0:
    break
  while(True):    
    if time == elt:
      print("you did it")

current_hour = dt.datetime.now().hour
current_min = dt.datetime.now().minute
alarm = any(i.hour == current_hour and i.minute == current_min for i in timetable)

print(alarm)

'''