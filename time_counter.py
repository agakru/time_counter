import time
from tkinter import *
from tkinter import ttk,messagebox
import tkinter
import openpyxl as op
import math
from PIL import Image, ImageTk

def start_time():
    filename="count_time.xlsx"
    workbook=op.load_workbook(filename)
    sheet=workbook.active
    while True: 
        try:
            workbook.save(filename=filename)
            break
        except PermissionError:
            print("Close your excel")
            messagebox.showerror(title="Python Error", message="Close your Excel!")
            time.sleep(2)

    st=math.floor(time.time())
    result=time.localtime(st)    
    date_string=time.strftime("%d/%m/%Y",result)
    time_string=time.strftime("%H:%M:%S",result)
    sheet.insert_rows(idx=2)
    sheet["A2"]= date_string
    sheet["B2"]= time_string
    sheet["D2"]= st
  
    button1.config(state=DISABLED)
    button2.config(state=NORMAL)
    c.itemconfig(label2,text=" ")
    c.itemconfig(label4,text=" ")
    c.itemconfig(label1,text=time_string,
                font=("Times New Roman", 14))
    #label5.config(image=img, state=NORMAL)
    workbook.save(filename=filename)
    workbook.close()

def end_time():
    filename="count_time.xlsx"
    workbook=op.load_workbook(filename)
    sheet=workbook.active
    et=math.floor(time.time())
    result=time.localtime(et)
    time_string=time.strftime("%H:%M:%S",result)
    sheet["C2"]= time_string
    cell=sheet["D2"]
    st=cell.value
    work_time=time.gmtime(et-st)
    work_str=time.strftime("%H:%M:%S",work_time)
    sheet["D2"]=work_str

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
    button2.config(state=DISABLED)
    #label5.config(state=DISABLED)
    c.itemconfig(label2,text=time_string,
                font=("Times New Roman", 14))
    c.itemconfig(label4,text=work_str,
    font=("Times New Roman", 14))
    workbook.close()

root =tkinter.Tk()
root.title("Counting Times")
root.geometry("300x300")
c =tkinter.Canvas(root, width=300, height=300)
c.pack()

bg_path = Image.open("C:/Users/PIERWSZY/Desktop/Projekty/Git/git_kurs/clock.png")
bg_size = bg_path.resize((300,300))
bg1= ImageTk.PhotoImage(bg_size)
id= c.create_image(0,0,anchor="nw",image=bg1)

image_start = Image.open("C:/Users/PIERWSZY/Desktop/Projekty/Git/git_kurs/start.png")
img_st_size = image_start.resize((70,20))
img_st = ImageTk.PhotoImage(img_st_size)

button1=ttk.Button(root, text="Start",command=lambda: start_time(),state=NORMAL,image=img_st)
button1.place(x=40,y=30)
label1=c.create_text(80,20,text="Start time:",
                font=("Times New Roman", 14))  

image_stop = Image.open("C:/Users/PIERWSZY/Desktop/Projekty/Git/git_kurs/stop.png")
img_sp_size = image_stop.resize((70,20))
img_sp = ImageTk.PhotoImage(img_sp_size)
button2=ttk.Button(root, text="Stop",command=lambda: end_time(),state=DISABLED,image=img_sp)
button2.place(x=185,y=30)
label2 =c.create_text(225,20,text="Stop time:",
                font=("Times New Roman", 14))

label3 = c.create_text(150,115,text="Work time: ",
                font=("Times New Roman", 14)) 
label4 = c.create_text(150,156,text=" ",
                font=("Times New Roman", 14)) 

button3=ttk.Button(root, text="Quit", command=root.destroy)
button3.place(x=120,y=270)
#image1 = Image.open("C:/Users/PIERWSZY/Desktop/Projekty/Git/git_kurs/lets_go.png")
#img = image1.resize((150,80))
#img = ImageTk.PhotoImage(img)
#label5 = ttk.Label(root,state=DISABLED)
#label5.place(x=75,y=100)
root.mainloop()
