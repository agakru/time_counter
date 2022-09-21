from fileinput import filename
import time
from tkinter import *
from tkinter import ttk
import openpyxl as op
import pandas as pd

col_num=0
def start_time(row_num=0):
    filename="write_data.xlsx"
    workbook=op.load_workbook(filename)
    sheet=workbook.active
    st=time.time()
    result=time.gmtime(st)
    time_string=time.strftime("%d/%m/%Y, %H:%M:%S",result)
    sheet.insert_rows(idx=1)
    sheet["A1"]= time_string
    workbook.save(filename=filename)
    print(st)

def end_time():
    filename="write_data.xlsx"
    workbook=op.load_workbook(filename)
    sheet=workbook.active
    et=time.time()
    result=time.gmtime(et)
    time_string=time.strftime("%H:%M:%S",result)
    sheet["B1"]= time_string
    workbook.save(filename=filename)
    print(et)
    return(et)

root = Tk()
root.title("Counting Times")
root.geometry("250x250")

label1 = ttk.Label(root, text="Start counting time: ")
label1.place(x=0,y=0)
button1=ttk.Button(root, text="Start",command=start_time)
button1.place(x=50,y=25)
button2=ttk.Button(root, text="Stop",command=lambda: ed=end_time())
button2.place(x=150,y=25)
button3=ttk.Button(root, text="Quit", command=root.destroy)
button3.place(x=100,y=100)
root.mainloop()

ed=end_time()