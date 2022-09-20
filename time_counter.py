import time
from tkinter import *
from tkinter import ttk
from tracemalloc import start
from turtle import delay, left
def start_time():
    start_time=time.time()
    return(start_time)
def end_time():
    end_time=time.time()
    return(end_time)


root = Tk()
root.title("Counting Times")
frm=root.geometry("250x250")

label1 = ttk.Label(frm, text="Start counting time: ")
label1.place(x=0,y=0)
button1=ttk.Button(frm, text="Start", command=start_time)
button1.place(x=50,y=25)
button2=ttk.Button(frm, text="Stop",command=end_time )
button2.place(x=150,y=25)
button3=ttk.Button(frm, text="Quit", command=root.destroy)
button3.place(x=100,y=100)

s=start_time()
e=end_time()
fin_time=e-s
print(fin_time)
