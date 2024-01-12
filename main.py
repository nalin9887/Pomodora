from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .1
SHORT_BREAK_MIN = .1
LONG_BREAK_MIN = .3
rep=0
current_work="nothing"
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    label.config(text="Timer",fg=GREEN)
    canas.itemconfig(time,text="00:00")
    check.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    global current_work
    rep+=1


    if rep==8:
        time=LONG_BREAK_MIN*60
        current_work="Long Break"
        label.config(text=current_work,fg=GREEN)

    elif rep%2==0 :
       time=SHORT_BREAK_MIN*60
       current_work="Short Break"
       label.config(text=current_work,fg="orange")
    else:
        time=WORK_MIN*60
        current_work="Work Time"
        label.config(text=current_work,fg="#e2979c")



    countdown(time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:

        count_sec=f"0{count_sec}"
    if count_min<10:
        count_min=f"0{count_min}"
    canas.itemconfig(time,text=f"{count_min}:{count_sec}")

    if count>0:
        global timer
        timer=window.after(1000,countdown,count-1)
    else:
        start_timer()
        mark=""
        timing=math.floor(rep/2)
        for n in range(timing):
            mark+="✅"
        check.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pandrom")
window.config(padx=30,pady=30,bg=YELLOW)
canas=Canvas(width=350,height=254,bg=YELLOW,highlightthickness=0)
Img=PhotoImage(file="tomato.png")
canas.create_image(174,112,image=Img)
time=canas.create_text(174,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canas.grid(row=2,column=2)
label=Label(text="TIMER",bg=YELLOW,fg=GREEN,font=(FONT_NAME,42,"bold"))
label.grid(row=1,column=2)

button1=Button(text="Start",command=start_timer,highlightthickness=0)
button1.grid(row=3,column=1)

button2=Button(text="Reset",highlightthickness=0,command=reset)
button2.grid(row=3,column=3)

check=Label(text="",fg=GREEN,bg=YELLOW,font=(FONT_NAME,24,"bold"))
check.grid(row=4,column=2)








window.mainloop()
