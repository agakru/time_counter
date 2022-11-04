import time
from tkinter import *
from tkinter import ttk,messagebox
import tkinter
import openpyxl as op
import math
from PIL import Image, ImageTk
import os

ACTUAL_DATE="A2"
PREVIOUS_DATE="A3"
START_COUNTING_IN_STRING="B2"
END_COUNT="C2"
START_COUNTING_IN_SEC="D2"
SUM_TIME_PREVIOUS="E3"
SUM_TIME="E2"
TOTAL_DAY="F2"
RED=(255,0,0)
START_ROW=2
SIZE_OF_FONT=14
WIDTH=300
HEIGHT=300

def check_if_open(workbook, filename):
    while True: 
        try:
            workbook.save(filename = filename)
            break
        except PermissionError:
            PATH=os.path.abspath(filename)
            messagebox.showerror(title = "Python Error", message = f"Close your Excel!'\n'{PATH}")
            time.sleep(2)

def start_time():
    filename="count_time.xlsx"
    workbook=op.load_workbook(filename)
    sheet=workbook.active
    for row in sheet:
        if sheet[SUM_TIME_PREVIOUS] == ' ':
            sheet.delete_rows(row[0])

    start_counting=math.floor(time.time())
    result=time.localtime(start_counting)    
    date_string=time.strftime("%d/%m/%Y", result)
    time_string=time.strftime("%H:%M:%S", result)
    sheet.insert_rows(idx = START_ROW)
    sheet[ACTUAL_DATE]=date_string
    sheet[START_COUNTING_IN_STRING]=time_string
    sheet[START_COUNTING_IN_SEC]=start_counting

    button_start.config(state = DISABLED)
    button_stop.config(state = NORMAL)
    canvas.itemconfig(label_stop,text = " ")
    canvas.itemconfig(label_show_work_time,text = " ")
    canvas.itemconfig(label_start,text = time_string,
                font=("Times New Roman", SIZE_OF_FONT))
    
    check_if_open(workbook, filename)
    workbook.save(filename = filename)
    workbook.close()

def end_time():
    filename="count_time.xlsx"
    workbook=op.load_workbook(filename)
    sheet=workbook.active
    end_count=math.floor(time.time())
    result=time.localtime(end_count)
    time_string=time.strftime("%H:%M:%S", result)
    sheet[END_COUNT]=time_string
    start_counting=sheet[START_COUNTING_IN_SEC].value
    work_time=time.gmtime(end_count - start_counting)
    work_str=time.strftime("%H:%M:%S", work_time)
    sheet[START_COUNTING_IN_SEC]=work_str

    if sheet[ACTUAL_DATE].value == sheet[PREVIOUS_DATE].value:
        read_start_time_in_sec=sheet[START_COUNTING_IN_SEC].value
        read_sum_time=sheet[SUM_TIME_PREVIOUS].value
        hours_start, min_start, sec_start=read_start_time_in_sec.split(":")
        if read_sum_time != None:
            hours_end, min_end, sec_end=read_sum_time.split(":")
        else:
            hours_end, min_end, sec_end=(0, 0, 0)

        total_hours=int(hours_start) + int(hours_end)
        total_min=int(min_start) + int(min_end)
        total_sec=int(sec_start) + int(sec_end)

        if total_sec >= 60:
            extra_min=total_sec // 60
            total_sec=total_sec - (extra_min * 60)
            total_min=total_min + extra_min
        if total_min >= 60:
            extra_hours=total_min // 60
            total_min=total_min - (extra_hours * 60)
            total_hours=total_hours + extra_hours
        if total_hours > 24:
            total_day=total_hours // 24
            total_hours=total_hours - (total_day * 24)
            sheet[TOTAL_DAY]=total_day

        sumtime=str(total_hours) + ':' + str(total_min) + ":" + str(total_sec)
        sum_time=time.strptime(sumtime, "%H:%M:%S")
        sum_time=time.strftime("%H:%M:%S", sum_time)
        sheet[SUM_TIME]=sum_time
        sheet[SUM_TIME_PREVIOUS]=" "
    else:      
        sum_time=sheet[START_COUNTING_IN_SEC].value
        sheet[SUM_TIME]=sum_time
    
    check_if_open(workbook, filename)
    workbook.save(filename = filename)
    button_start.config(state = NORMAL)
    button_stop.config(state = DISABLED)

    canvas.itemconfig(label_stop, text=time_string,
                font=("Times New Roman", SIZE_OF_FONT))
    canvas.itemconfig(label_show_work_time, text=work_str,
                font=("Times New Roman bold", SIZE_OF_FONT))
    workbook.close()

root=tkinter.Tk()
root.title("Time Counter")
root.resizable(0,0)
canvas=tkinter.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

background_path = Image.open(os.path.abspath("clock.png"))
background_path.putalpha(60) 
background_size = background_path.resize((WIDTH, HEIGHT))
background_img= ImageTk.PhotoImage(background_size)
background= canvas.create_image(0, 0, anchor="nw", image=background_img)

image_start_path = Image.open(os.path.abspath("start.png"))
img_start_size = image_start_path.resize((70, 20))
img_start = ImageTk.PhotoImage(img_start_size)

button_start=ttk.Button(root, text="Start", command=lambda: start_time(), state=NORMAL, image=img_start)
button_start.place(x=40, y=30)
label_start=canvas.create_text(80, 20, text="Start time:",
                font=("Times New Roman", SIZE_OF_FONT))  

image_stop = Image.open(os.path.abspath("stop.png"))
img_stop_size = image_stop.resize((70, 20))
img_stop = ImageTk.PhotoImage(img_stop_size)
button_stop=ttk.Button(root, text="Stop", command=lambda: end_time(), state=DISABLED, image=img_stop)
button_stop.place(x=185, y=30)
label_stop =canvas.create_text(225, 20, text="Stop time:",
                font=("Times New Roman", SIZE_OF_FONT))

label_work_time = canvas.create_text(150, 115, text="Work time: ",
                font=("Times New Roman underline", SIZE_OF_FONT)) 
label_show_work_time = canvas.create_text(150, 156, text=" ",
                font=("Times New Roman bold underline", SIZE_OF_FONT,)) 

button_quit=ttk.Button(root, text="Quit", command=root.destroy)
button_quit.place(x=115, y=270)

root.mainloop()
