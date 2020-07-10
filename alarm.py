#!/usr/bin/python

import os
import sys
from tkinter import *
from tkinter.ttk import *
import datetime as dt
from time import strftime
import time
from playsound import playsound


#Getting Time Table
t1 = dt.time(hour = 14, minute= 17)
t2 = dt.time(hour= 14, minute= 29)
timetable = [t1, t2]
#timetable = ["11:05", "11:09"]

#Creating Window and Label
root = Tk() 
root.title('Alarm Clock') 

now_time = dt.datetime.now()
  
# This function is used to  
# display time on the label 
def time(): 
    string = now_time.strftime("%H:%M:%S")
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

frame1 = Frame(root)

frame1.config(height = 500, width = 500)
frame1.pack()
alm = Label(frame1)
alm.pack()

'''
# Working Alarm Clock
for i in timetable:
    current_time = dt.datetime.now().time()
    alarm_time = i
    while True:
        if current_time < alarm_time:
            if current_time <= alarm_time:
                print("its time", alarm_time)

#Test Alarm Clock
#def alarm():
for i in reversed(timetable):
    i_time = i
    #print (i_time)
    #print(now_time.strftime("%H:%M"))
    while True:
        if dt.datetime.now().time() < i_time:
        #if i_time <= dt.datetime.now().time():
            #playsound('media/ClassAlarm.mp3', False)
            #alm.config(text= "Its Time to end class")
            print("Its Time")
            break
    #else:
        #alm.config(text= "Time till class end:" + i_time.strftime("%H:%M"))

'''
root.mainloop()
