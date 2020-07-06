#!/usr/bin/python

import os
import sys
from tkinter import *
from tkinter.ttk import *
import datetime as dt
from playsound import playsound


#Getting Time Table
t1 = dt.time(hour = 17, minute= 29)
t2 = dt.time(hour= 17, minute= 35)
timetable = [t1, t2]

#Creating Window and Label
root = Tk() 
root.title('Alarm Clock') 
  
# This function is used to  
# display time on the label 
def time(): 
    string = dt.datetime.now()
    lbl.config(text = string) 
    lbl.after(1000, time) 
  
# Styling the label widget so that clock 
# will look more attractive 
lbl = Label(root, font = ('calibri', 40, 'bold'), 
            background = 'green', 
            foreground = 'white') 
  
# Placing clock at the centre 
# of the tkinter window 
lbl.pack(anchor = 'center') 
time() 
  

#def alarm():
for elt in timetable:
    i_time = elt
    #i_minute = i.minute
    while True:
        if i_time <= dt.datetime.now().time():
            playsound('media/ClassAlarm.mp3', False)
            alm.config(text= "Its Time to end class")
            break

frame1 = Frame(root)
frame1.pack()
frame1.config(height = 100, width = 100)

alm = Label(frame1)
alm.pack()

root.mainloop()

