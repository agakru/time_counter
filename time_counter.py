import time
from tkinter import *
from tkinter import ttk
from xml.dom import minicompat
import openpyxl as op
import math

def start_time():
    filename="count_time.xlsx"
    workbook=op.load_workbook(filename)
    sheet=workbook.active
    st=time.time()
    result=time.localtime(st)    
    date_string=time.strftime("%d/%m/%Y",result)
    time_string=time.strftime("%H:%M:%S",result)
    sheet.insert_rows(idx=2)
    sheet["A2"]= date_string
    sheet["B2"]= time_string
    sheet["D2"]= st
    workbook.save(filename=filename)
    button1.config(state=DISABLED)

def end_time():
    filename="count_time.xlsx"
    workbook=op.load_workbook(filename)
    sheet=workbook.active
    et=time.time()
    result=time.localtime(et)
    time_string=time.strftime("%H:%M:%S",result)
    sheet["C2"]= time_string
    cell=sheet["D2"]
    st=cell.value
    work_time=time.gmtime(et-st)
    work_str=time.strftime("%H:%M:%S",work_time)
    sheet["D2"]=work_str
    label2.config(text=work_str)
    if sheet["A2"].value==sheet["A3"].value:
        cell1=sheet["D2"].value
        cell2=sheet["E3"].value
        a=cell1.split(":")
        hours1=int(a[0])
        min1=int(a[1])
        sec1=int(a[2])
        b=cell2.split(":")
        hours2=int(b[0])
        min2=int(b[1])
        sec2=int(b[2])
        total_hours=hours1+hours2
        total_min=min1+min2
        total_sec=sec1+sec2
       
        if total_min>=60:
            extra_hours=total_min//60
            total_min=total_min-(extra_hours*60)
            total_hours=total_hours+extra_hours
        if total_sec>=60:
            extra_min=total_sec//60
            total_sec=total_sec-(extra_min*60)
            total_min=total_min+extra_min
        sumtime=str(total_hours)+':'+ str(total_min)+":"+ str(total_sec)
        sum_time=time.strptime( sumtime,"%H:%M:%S")
        sum_time=time.strftime("%H:%M:%S",sum_time)
        sheet["E2"]=sum_time
        sheet["E3"]=" "
    else:      
        sum_time=sheet["D2"].value
        sheet["E2"]=sum_time
    workbook.save(filename=filename)
    button1.config(state=NORMAL)

root = Tk()
root.title("Counting Times")
root.geometry("300x200")

label1 = ttk.Label(root, text="Start counting time: ")
label1.place(x=0,y=0)
button1=ttk.Button(root, text="Start",command=lambda: start_time(),state=NORMAL)
button1.place(x=50,y=50)
button2=ttk.Button(root, text="Stop",command=lambda: end_time())
button2.place(x=175,y=50)
label2 = ttk.Label(root, text="Here will be yor working time!")
label2.place(x=125,y=100)
button3=ttk.Button(root, text="Quit", command=root.destroy)
button3.place(x=110,y=150)
root.mainloop()

