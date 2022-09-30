# creating a digital clock with python, tkinter package

# from logging import root
# importing tkinter package
from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

def quit(*args):
    root.destroy()  # will case the loop to exit

    def clockTime():
        time = datetime.datetime.now()
        time = (time.strftime("%H:%M:%S"))
        txt.set(time)
        root.after(1000,clockTime)

# setting gui specifications
root = Tk()
root.attributes("-fullscreen", False)
root.configure(background="black")
root.bind("x", quit)
# root.after(1000,clockTime)

fnt = font.Font(family="Helvetica", size=120,weight="bold")
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="white", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()


