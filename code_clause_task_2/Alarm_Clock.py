from threading import Thread
from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
from PIL import ImageTk,Image
from pygame import mixer
from datetime import datetime
from time import sleep
#from sklearn.feature_selection import SelectFdr

window=Tk()
window.geometry("350x150")
window.title("Alarm_Clock")
window.iconbitmap("alarm2.ico")
global Selected
Selected=IntVar()
Selected.set(None)

def Activate_alarm():
    t=Thread(target=alarm)
    t.start()
def deactivate_alarm():
    print("deactivated alarm:",Selected.get())
    mixer.music.stop()

def sound_alarm():
    mixer.music.load("tense-cinematic-117406.mp3")
    mixer.music.play()
    Selected.set(0)
    rad2=Radiobutton(frame_body,font=("arial 10 bold"),text="DeActivate",bg="lightgreen",command=deactivate_alarm,value=2,variable=Selected)
    rad2.place(x=187,y=95)

def alarm():
    while True:
        control=Selected.get()
        print(control)
        alarm_hour=c_hours.get()
        alarm_mintue=c_mintues.get()
        alarm_second=c_sections.get()
        alarm_period=c_period.get()
        alarm_period=str(alarm_period).upper()
        hour=datetime.now().strftime("%I")
        minute=datetime.now().strftime("%M")
        second=datetime.now().strftime("%S")
        period=datetime.now().strftime("%p")
        if control==1:
            if alarm_period==period:
                if alarm_hour==hour:
                    if alarm_mintue==minute:
                        if alarm_second==second:
                            sound_alarm()
        sleep(1)



mixer.init()


frame_line=Frame(window,width=400,height=5,bg="#566fC6")
frame_line.grid(row=0,column=0)
frame_body=Frame(window,width=400,height=290,bg="white")
frame_body.grid(row=1,column=0)

img=Image.open("alarmclock.ico")
img.resize((100,100))
img=ImageTk.PhotoImage(img)

image=Label(frame_body,height=100,image=img)
image.place(x=10,y=10)

name=Label(frame_body,text="Alarm",height=1,font=('Ivy 18 bold'),bg="white")
name.place(x=125,y=10)

hours=Label(frame_body,text="Hours",height=1,font=('arial 10  bold'),bg="white",fg="#566fC6")
hours.place(x=127,y=40)
c_hours=Combobox(frame_body,width=2,font=("arial 15"))
c_hours['values']=('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24')
c_hours.current(0)
c_hours.place(x=130,y=58)


minutes=Label(frame_body,text="Minutes",height=1,font=('arial 10  bold'),bg="white",fg="#566fC6")
minutes.place(x=177,y=40)
c_mintues=Combobox(frame_body,width=2,font=("arial 15"))
c_mintues['values']=('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60')
c_mintues.current(0)
c_mintues.place(x=180,y=58)

seconds=Label(frame_body,text="Secondes",height=1,font=('arial 10  bold'),bg="white",fg="#566fC6")
seconds.place(x=227,y=40)
c_sections=Combobox(frame_body,width=2,font=("arial 15"))
c_sections['values']=('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60')
c_sections.current(0)
c_sections.place(x=230,y=58)

periods=Label(frame_body,text="Period",height=1,font=('arial 10  bold'),bg="white",fg="#566fC6")
periods.place(x=277,y=40)
c_period=Combobox(frame_body,width=4,font=("arial 15"))
c_period['values']=("AM","PM")
c_period.current(0)
c_period.place(x=280,y=58)

rad1=Radiobutton(frame_body,font=("arial 10 bold"),text="Activate",bg="lightgreen",command=Activate_alarm,value=1,variable=Selected)
rad1.place(x=125,y=95)


window.mainloop()
