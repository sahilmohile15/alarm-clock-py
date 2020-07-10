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
import threading
from pygame import mixer
import webbrowser

root = Tk()
root.title('Alarm Clock') 

now_time = dt.datetime.now().time()


#Start Time-Table
st1 = dt.time(hour = 17, minute= 33)
st2 = dt.time(hour= 16, minute= 46)
st3 = dt.time(hour= 10, minute=50)
st4 = dt.time(hour= 11, minute=20)
st5 = dt.time(hour= 12, minute=20)
st6 = dt.time(hour= 14, minute=20)

#Creating an array of time-table
sTimetable = [st1, st2, st3, st4, st5, st6]

#End Time Table
t1 = dt.time(hour = 17, minute= 33)
t2 = dt.time(hour= 16, minute= 46)
t3 = dt.time(hour= 10, minute=50)
t4 = dt.time(hour= 11, minute=20)
t5 = dt.time(hour= 12, minute=20)
t6 = dt.time(hour= 14, minute=20)


#Creating an array of End time-table
timetable = [t1, t2, t3, t4, t5, t6]
#timetable = ["13:18:00", "13:12"]


#Clock Function
def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200, tick)

clock=Label(root, font=("times", 50, "bold"), bg= "white")
clock.grid(row=0, column=1)

def browser(url, p, do):
      if do == True:
            p = sp.Popen("Chrome", url)

      if do == False:
            p.kill()

def Start():
      while True:
            current_time = dt.datetime.now().time()
            for i in range(6):
                  if sTimetable[i] == current_time:
                        browser(do = True)
                        time.sleep(10)
                        s_string = "The Class is Started..."
                        s.config(text=s_string)
                        break

s = Label(root, font=("times", 50), bg= "grey")
s.pack()

def Alarm():
      while True:
            current_time = dt.datetime.now().time()
            if timetable[0] == current_time:
                  mixer.init()
                  mixer.music.load("media/ClassAlarm.wav")
                  mixer.music.play()
                  browser(do = False)
                  e_string = "The Time for Class has Ended... Waiting for next Class"
                  e.config(text=e_string)
                  break
            elif timetable[1] == current_time:
                  mixer.init()
                  mixer.music.load("media/ClassAlarm.wav")
                  mixer.music.play()
                  browser(do = False)
                  e_string = "The Time for Class has Ended... Waiting for next Class"
                  e.config(text=e_string)
                  break
            elif timetable[2] == current_time:
                  mixer.init()
                  mixer.music.load("media/ClassAlarm.wav")
                  mixer.music.play()
                  browser(do = False)
                  e_string = "The Time for Class has Ended... Waiting for next Class"
                  e.config(text=e_string)
                  break
            elif timetable[3] == current_time:
                  mixer.init()
                  mixer.music.load("media/ClassAlarm.wav")
                  mixer.music.play()
                  browser(do = False)
                  e_string = "The Time for Class has Ended... Waiting for next Class"
                  e.config(text=e_string)
                  break
            elif timetable[4] == current_time:
                  mixer.init()
                  mixer.music.load("media/ClassAlarm.wav")
                  mixer.music.play()
                  browser(do = False)
                  e_string = "The Time for Class has Ended... Waiting for next Class"
                  e.config(text=e_string)
                  break
            elif timetable[5] == current_time:
                  mixer.init()
                  mixer.music.load("media/ClassAlarm.wav")
                  mixer.music.play()
                  browser(do = False)
                  e_string = "The Time for Class has Ended... Waiting for next Class"
                  e.config(text=e_string)
                  break

e = Label(root, font=("times", 50), bg= "grey")
e.pack()
tick()

start_thread = threading.Thread(target=Start)
alarm_thread = threading.Thread(target=Alarm)
#main_thread = threading.Thread(target=root.mainloop)

start_thread.start()
alarm_thread.start()
#main_thread.start()

root.mainloop()

'''
def browse(url, how_long):
    child = sp.Popen("chrome %s" % url, shell=True)
    time.sleep(how_long)
    child.terminate()
browse("http://www.python.org", 3)
'''