from tkinter import *
import tkinter
import tkinter.messagebox as msgbox
import time


rot=Tk()
rot.title("자동 2차 함수 계산")
rot.geometry("1020x1120")
rot_frame=Frame(rot)
rot_frame.pack()

txt_frame=Frame(rot_frame)
txt_frame.pack(side="left")

txt=Text(txt_frame, width=30, height=2)
txt.pack(side="left")



def insert():
    global txt
    text=txt.get(1.0, tkinter.END)
    x=-5
    for i in range(0, 11):
        lis=eval(text)
        list_box.insert(i, str(x)+","+str(lis))
        x+=1

def draw():
    global list_box
    list_box.delete(0,END)
    
    x=-10
    text=txt.get(1.0, tkinter.END)
    global label
    for i in range(201):
        lists=eval((text))
        x+=0.1
        a=eval((text))
        canvas.create_line(float((500+(x*20))), float(1000-(500+lists*20)), float((500+(x+0.1)*20)), float(1000-(500+a*20)), fill="blue", width=2, tags=("label",))
        
    
    

    x=-10
    for i in range(10):
        lis=eval((text))
        
        canvas.create_text(int((500+(x*20))-50), int(1005-(500+lis*20)), text =str(x)+","+str(eval(text)), font = ("나눔고딕코딩", 20), fill = "green", tags=("label",))
        x+=1

    for i in range(10):
        lis=eval((text))
        
        canvas.create_text(int((500+(x*20))+50), int(1005-(500+lis*20)), text =str(x)+","+str(eval(text)), font = ("나눔고딕코딩", 20), fill = "green", tags=("label",))
        x+=1
    insert()

def asd():
    list_box.delete(0,END)
    canvas.delete("label")

OK=Button(rot_frame, padx=8, pady=5, width=4,text="확인", command=draw)
OK.pack(padx=8, pady=5, side="left")

Del=Button(rot_frame, padx=8, pady=5, width=4,text="삭제", command=asd)
Del.pack(padx=8, pady=5, side="left")

list_box=Listbox(rot_frame, selectmode="extended", height=0)
list_box.pack(side="right")

canvas=Canvas(rot, width=1020, height=1020, bg="white", bd=0)
canvas.pack(side="bottom")

height=20
w=20

for xq in range(20, 1020, 20):
    canvas.create_line(xq,0, xq,1000, fill="black")
    if height==500:
        canvas.create_line(xq,0, xq,1000,fill="blue", width=2)
    height+=20

for yq in range(20, 1020, 20):
    canvas.create_line(0,yq, 1000,yq, fill="black")
    if w==500:
        canvas.create_line(0,yq, 1000,yq, fill="blue", width=2)
    w+=20


rot.resizable(True, True)
rot.mainloop()