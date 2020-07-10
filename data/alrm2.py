#!/usr/bin/python

import os
import sys
from tkinter import *
from tkinter.ttk import *
import datetime as dt
from time import strftime
from tkinter import *
import time
import subprocess as sp


root = Tk()
root.title('Alarm Clock') 

now_time = dt.datetime.now().time()
  
#Getting Time Table
t1 = dt.time(hour = 13, minute= 48)
t2 = dt.time(hour= 13, minute= 46)
t3 = dt.time(hour= 10, minute=50)
t4 = dt.time(hour= 11, minute=20)
t5 = dt.time(hour= 12, minute=20)
t6 = dt.time(hour= 14, minute=20)
timetable = [t1, t2, t3, t4, t5, t6]
#timetable = ["13:18:00", "13:12"]

def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200, tick)

clock=Label(root, font=("times", 50, "bold"), bg= "white")
clock.grid(row=0, column=1)


tick()


def Alarm():
      while True:
            current_time = dt.datetime.now().time()
            if timetable[0] == current_time:
                  print("Its time")
                  break
            elif timetable[1] == current_time:
                  print("Its second alarm")
                  break
            elif timetable[2] == current_time:
                  print("Its third Alarm")
                  break
            elif timetable[3] == current_time:
                  print("Its fourth Alarm")
                  break
            elif timetable[4] == current_time:
                  print("Its fifth Alarm")
                  break
            elif timetable[5] == current_time:
                  print("Its sixth Alarm")
                  break
            elif timetable[6] == current_time:
                  print("Its seventh Alarm")
                  break
            
Alarm()



def browse(url, how_long):
    child = sp.Popen("chrome %s" % url, shell=True)
    time.sleep(how_long)
    child.terminate()
browse("http://www.python.org", 3)
root.mainloop()
