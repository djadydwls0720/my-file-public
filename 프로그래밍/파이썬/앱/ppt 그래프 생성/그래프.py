from tkinter import *
import tkinter
import requests
from bs4 import BeautifulSoup
import re
import csv
from PIL import ImageGrab
import math

color_list=[]
rkqt_list=[]
name_list=[]

def reset():
    canvas.delete("number")
    global bar_one_x, bar_two_x,rkqt_list
    i=0
    try:
        i=eval(txt.get(1.0, tkinter.END))

    except SyntaxError:
        i=max(rkqt_list)
        i=round(i+i/6, 3)
    a=1
    vusck=0
    canvas.delete("label_num")
    canvas.create_text(18, 580, text="0", tags=("label_num",))
    for y in range(100, 600, 100):
        canvas.create_text(18, y, text=str(int(i*a)), tags=("label_num",))
        a-=0.2

    

    #그래프 x길이:850 
    #바 기본 길이:250
    for rkq in range(0, int(len(rkqt_list)),1):
        canvas.create_text(bar_one_x+(850/graph_bar)*rkq+((bar_two_x-bar_one_x)/2), 600, text=(str(name_list[rkq])), tags=("number",), font=("나눔고딕코딩",13))

    if on_off_var_th.get()==1:
        for rqk in range(0, int(len(rkqt_list)), 1):
            vusck+=rkqt_list[rqk]

        vusck=vusck/int(len(rkqt_list))

        canvas.create_line(50, 580-(480*(float(vusck)/i)), 900,580-(480*(float(vusck)/i)), tags=("number"), fill="blue", width=2)

        if vusck%1==0:
            canvas.create_text(70, 580-(480*(float(vusck)/i))-15, text=str(int(vusck)),tags=("number"), fill="blue",font=(15))
        else:
            canvas.create_text(70, 580-(480*(float(vusck)/i))-15, text=str(round(float(vusck),1)),tags=("number"), fill="blue",font=(15))
        for rkq in range(0, int(len(rkqt_list)), 1):

            if abs(rkqt_list[rkq]-vusck)%1==0:
                if rkqt_list[rkq]-vusck>0:

                    canvas.create_text(bar_one_x+(850/graph_bar)*rkq+((bar_two_x-bar_one_x)/2), 580-(480*(float(rkqt_list[rkq])/i))-30, text="+"+str(int(rkqt_list[rkq]-vusck)), tags=("number",), font=("나눔고딕코딩",13), fill="red")
                else:
                    canvas.create_text(bar_one_x+(850/graph_bar)*rkq+((bar_two_x-bar_one_x)/2), 580-(480*(float(rkqt_list[rkq])/i))-30, text=str(int(rkqt_list[rkq]-vusck)), tags=("number",), font=("나눔고딕코딩",13), fill="blue")

            else:
                if rkqt_list[rkq]-vusck>0:
                    canvas.create_text(bar_one_x+(850/graph_bar)*rkq+((bar_two_x-bar_one_x)/2), 580-(480*(float(rkqt_list[rkq])/i))-30, text="+"+(str(round(float(rkqt_list[rkq]-vusck),1))), tags=("number",), font=("나눔고딕코딩",13), fill="red")
                else:
                    canvas.create_text(bar_one_x+(850/graph_bar)*rkq+((bar_two_x-bar_one_x)/2), 580-(480*(float(rkqt_list[rkq])/i))-30, text=(str(round(float(rkqt_list[rkq]-vusck),1))), tags=("number",), font=("나눔고딕코딩",13), fill="blue")
                    
    if on_off_var.get()==1:
        for rkq in range(0, int(len(rkqt_list)), 1):
            canvas.create_rectangle(bar_one_x+(850/graph_bar)*rkq, 580, bar_two_x+(850/graph_bar)*rkq, 580-(480*(float(rkqt_list[rkq])/i)), fill=color_list[rkq], tags=("label_num",))
            if rkqt_list[rkq]%1==0:
                canvas.create_text(bar_one_x+(850/graph_bar)*rkq+((bar_two_x-bar_one_x)/2), 580-(480*(float(rkqt_list[rkq])/i))-15, text=(int(rkqt_list[rkq])), tags=("number",), font=("나눔고딕코딩",10))
            elif rkqt_list[rkq]%1!=0:
                canvas.create_text(bar_one_x+(850/graph_bar)*rkq+((bar_two_x-bar_one_x)/2), 580-(480*(float(rkqt_list[rkq])/i))-15, text=(float(rkqt_list[rkq])), tags=("number",), font=("나눔고딕코딩",10))

    if on_off_var_t.get()==1:
        for rkq in range(0, int(len(rkqt_list)), 1):
            if rkqt_list[rkq]%1==0:
                    canvas.create_text(bar_one_x+(850/graph_bar)*rkq+((bar_two_x-bar_one_x)/2), 580-(480*(float(rkqt_list[rkq])/i))-15, text=str(int(rkqt_list[rkq])), tags=("number",), font=("나눔고딕코딩",10))
            else:
                canvas.create_text(bar_one_x+(850/graph_bar)*rkq+((bar_two_x-bar_one_x)/2), 580-(480*(float(rkqt_list[rkq])/i))-15, text=str(float(rkqt_list[rkq])), tags=("number",), font=("나눔고딕코딩",10))
        
        for rkq in range(0, int(len(rkqt_list)), 1):
            canvas.create_rectangle(bar_one_x+(850/graph_bar)*rkq+((bar_two_x-bar_one_x)/2)-4, 580-(480*(float(rkqt_list[rkq])/i))-4, bar_one_x+(850/graph_bar)*rkq+((bar_two_x-bar_one_x)/2)+4, 580-(480*(float(rkqt_list[rkq])/i))+4, fill=color_var_t.get(), tags=("label_num",))
            canvas.create_line(bar_one_x+(850/graph_bar)*rkq+((bar_two_x-bar_one_x)/2), 580-(480*(float(rkqt_list[rkq])/i)), bar_one_x+(850/graph_bar)*(rkq+1)+((bar_two_x-bar_one_x)/2), 580-(480*(float(rkqt_list[rkq+1])/i)), fill=color_var_t.get(), tags=("label_num",), width=2)

def dksl():
    global bar, graph_bar, bar_rlfdl,  bar_one_x, bar_two_x
    if graph_bar<=0:
        graph_bar=1
        bar=1

    bar_rlfel=(bar_rlfdl/graph_bar)
    bar-=1
    graph_bar-=1

    if graph_bar<=0:
        graph_bar=1
        bar=1

    num_t=int(len(color_list)-1)

    if num_t<0:
        num_t=0
    x_a=(50+((850/graph_bar)))
    x_d=(50+((850/graph_bar)+bar_rlfel))


    bar_one_x=int(x_a-((x_d-x_a)/2))
    bar_two_x=int(x_d-((x_d-x_a)/2))

    del color_list[num_t]
    del rkqt_list[num_t]
    del name_list[num_t]
    reset()


def graph_bar_becoming(rkqt, name):
    
    global graph_bar, bar_one_x, bar_two_x, bar, co
    if graph_bar<=0:
        graph_bar=1
        bar=1
    bar_rlfel=(bar_rlfdl/graph_bar)
    
    graph_bar+=1
    bar+=1
    x_a=(50+((850/graph_bar)))
    x_d=(50+((850/graph_bar)+bar_rlfel))
    
    color_list.append(color_var.get())

    bar_one_x=int(x_a-((x_d-x_a)/2))
    bar_two_x=int(x_d-((x_d-x_a)/2))

    rkqt_list.append(rkqt)
    name_list.append(name)

    print(bar_one_x)
    print(bar_two_x)
    reset()

def tnwjd():
    becoming_window=Tk()
    becoming_window.title("바 생성")
    becoming_window.geometry("170x80")

    FRAMe=Frame(becoming_window)
    FRAMe.pack()

    frame2=Frame(FRAMe)
    frame2.pack(side="right", padx=3)
    
    def graph_bar_becoming_wjs():
        a=float(eval(entry.get()))
        n=str(entry2.get())
        graph_bar_becoming(a,n) 

    rkqt=Frame(FRAMe)
    rkqt.pack(side="left", padx=3)

    label=Label(rkqt,text="값:")
    label.pack()

    entry= Entry(rkqt, width=10)
    entry.pack()

    label2=Label(frame2,text="이름:")
    label2.pack()

    entry2= Entry(frame2, width=10)
    entry2.pack()

    Ok=Button(becoming_window, text="확인", command=graph_bar_becoming_wjs)
    Ok.pack(pady=3)


    
    becoming_window.resizable(False, False)
    becoming_window.mainloop()


def name():
    Name=Tk()
    Name.title("그래프 이름")
    Name.geometry("150x80")
    label=Label(Name, text="이름:")
    label.pack()

    entry= Entry(Name, width=10)
    entry.pack()

    def ok():
        canvas.delete("name")
        canvas.create_text(475, 50, text=str(entry.get()), tags=("name",), font=("나눔고딕코딩",50))

    Ok=Button(Name, text="확인", command=ok)
    Ok.pack(pady=3)

def Ok_let():
    reset()

def eksdnl_vytl():
    Name=Tk()
    Name.title("그래프 단위 이름")
    Name.geometry("150x80")
    label=Label(Name, text="이름:")
    label.pack()

    entry= Entry(Name, width=10)
    entry.pack()

    def ok():
        
        canvas.delete("nameeksdnl")
        canvas.create_text(840, 40, text=str("(단위:"+entry.get()+")"), tags=("nameeksdnl",), font=("나눔고딕코딩",18))
        
        reset()

    Ok=Button(Name, text="확인", command=ok)
    Ok.pack(pady=3)
    
def save():

    save_window=Tk()
    save_window.title("그래프 저장")
    save_window.geometry("120x80")

    FRAMe=Frame(save_window)
    FRAMe.pack()

    frame2=Frame(FRAMe)
    frame2.pack(side="right", padx=3)
    
    def save_file():
        x = rot.winfo_rootx()  #창의 왼쪽 위의 x 좌표
        y = rot.winfo_rooty()  #창의 왼쪽 위의 y 좌표
        w = rot.winfo_width() + x
        h = rot.winfo_height() + y

        print(str(rot.winfo_width()))
        print(str(rot.winfo_height()))

        box = (x+349, y+35, w-28, h)
        img=ImageGrab.grab(box) #창의 크기만큼만 이미지저장
        saveas=save_entry.get()+'.png'
        img.save(saveas) # 이미지를 파일로 저장

    save_rkqt=Frame(FRAMe)
    save_rkqt.pack(padx=3)

    save_label=Label(save_rkqt,text="파일 이름")
    save_label.pack()

    save_entry= Entry(save_rkqt, width=10)
    save_entry.pack()

    Ok=Button(save_window, text="확인", command=save_file)
    Ok.pack(pady=3)
    
    save_window.resizable(False, False)
    save_window.mainloop()

def clickMouse(event):
    global bar_one_x, graph_bar, rkqt_list, name_list, color_list


    i=0
    try:
        i=eval(txt.get(1.0, tkinter.END))

    except SyntaxError:
        i=max(rkqt_list)
        i=round(i+i/6, 3)

    def editWindow(a):
        index=a

        edit_window=Tk()
        edit_window.title("바 생성")
        edit_window.geometry("170x80")

        edit_FRAMe=Frame(edit_window)
        edit_FRAMe.pack()

        edit_frame2=Frame(edit_FRAMe)
        edit_frame2.pack(side="right", padx=3)
                


        def edit():
            rkqt_list[index]=eval(edit_entry.get())
            name_list[index]=edit_entry2.get()
            reset()
            


        edit_rkqt=Frame(edit_FRAMe)
        edit_rkqt.pack(side="left", padx=3)

        edit_label=Label(edit_rkqt,text="값:")
        edit_label.pack()

        edit_entry= Entry(edit_rkqt, width=10)

        if rkqt_list[a]%1==0:
            edit_entry.insert(0, int(rkqt_list[a]))
        else:
            edit_entry.insert(0, rkqt_list[a])

        edit_entry.pack()

        edit_label2=Label(edit_frame2,text="이름:")
        edit_label2.pack()

        edit_entry2= Entry(edit_frame2, width=10)
        edit_entry2.insert(0, name_list[a])
        edit_entry2.pack()

        edit_color_frame=Frame(edit_window)
        edit_color_frame.pack()

        edit_color_frame1=Frame(edit_color_frame)
        edit_color_frame1.pack(side="left")
                
        edit_color_frame2=Frame(edit_color_frame)
        edit_color_frame2.pack(side="left")


        edit_Ok=Button(edit_window, text="확인", command=edit)
        edit_Ok.pack(pady=3)
                
        edit_window.resizable(False, False)
        edit_window.mainloop()



    for a in range(0, int(len(rkqt_list))):
        if bar_one_x+(850/graph_bar)*a<event.x and bar_two_x+(850/graph_bar)*a>event.x:
            if 580>event.y and 580-(480*(float(rkqt_list[a])/i))<event.y:
                editWindow(a)
                



graph_bar=1
bar_rlfdl=200
bar=1


rot=Tk()
rot.title("그래프")
rot.geometry("1320x650")

txt_frame=Frame(rot)
txt_frame.pack(side="left", fill="x")


rot.bind("<Button>",clickMouse)


txt_label=Label(txt_frame,text="최대 값:")
txt_label.pack()
txt=Text(txt_frame, width=10, height=1)
txt.pack()

OK=Button(txt_frame, text="확인", command=reset)
OK.pack(pady=4, padx=4)

bar_becoming=Button(txt_frame, text="바 생성", command=tnwjd)
bar_becoming.pack()

Del=Button(txt_frame, text="삭제", command=dksl)
Del.pack()

color_frame=Frame(rot)
color_frame.pack(side="left")

color_label=Label(color_frame, text="막대 그래프 색상")
color_label.pack()

color_var=StringVar()
color_Rad=Radiobutton(color_frame, text="빨강", value="red", variable=color_var)
color_Rad.pack()

color_yellow=Radiobutton(color_frame, text="노랑", value="yellow", variable=color_var)
color_yellow.pack()

color_black=Radiobutton(color_frame, text="검정", value="black", variable=color_var)
color_black.pack()

color_blue=Radiobutton(color_frame, text="파랑", value="blue", variable=color_var)
color_blue.select()
color_blue.pack()

color_green=Radiobutton(color_frame, text="초록", value="green", variable=color_var)
color_green.pack()

color_sky=Radiobutton(color_frame, text="하늘", value="skyblue", variable=color_var)
color_sky.pack()

color_frame_t=Frame(rot)
color_frame_t.pack(side="left")


color_var_t=StringVar()
color_Rad_t=Radiobutton(color_frame_t, text="빨강", value="red", variable=color_var_t)
color_Rad_t.pack()

color_yellow_t=Radiobutton(color_frame_t, text="노랑", value="yellow", variable=color_var_t)
color_yellow_t.pack()

color_black_t=Radiobutton(color_frame_t, text="검정", value="black", variable=color_var_t)
color_black_t.pack()

color_blue_t=Radiobutton(color_frame_t, text="파랑", value="blue", variable=color_var_t)
color_blue_t.pack()

color_green_t=Radiobutton(color_frame_t, text="초록", value="green", variable=color_var_t)
color_green_t.pack()
color_green_t.select()

color_green_t=Radiobutton(color_frame_t, text="하늘", value="skyblue", variable=color_var_t)
color_green_t.pack()

on_off_frame=Frame(rot)
on_off_frame.pack(side="left")

on_off_var=IntVar()
on_off_var_t=IntVar()
on_off_var_th=IntVar()

stic_btn=Checkbutton(on_off_frame, text="막대 그래프", variable=on_off_var)
stic_btn.pack()
stic_btn.select()

line_btn=Checkbutton(on_off_frame, text="직선 그래프", variable=on_off_var_t)
line_btn.pack()

vusck_btn=Checkbutton(on_off_frame, text="편차 값 표시", variable=on_off_var_th)
vusck_btn.pack()

Ok_on_off=Button(on_off_frame, text="확인", command=Ok_let)
Ok_on_off.pack()

rot_frame=Frame(rot)
rot_frame.pack(side="top")

name_btn=Button(rot_frame,text="그래프 이름", command=name)
name_btn.pack(pady=3, side="left")

tkrkrgud=canvas=Canvas(rot, width=940, height=700, bg="white", bd=0)
canvas.pack(side="right", expand=True)
canvas.create_rectangle(50, 580, 900, 100)

eksdnl=Button(rot_frame, text="단위 표기", command=eksdnl_vytl)
eksdnl.pack(padx=5, pady=3, side="left")

wjwkd=Button(rot_frame, text="캡쳐", command=save)
wjwkd.pack(padx=5, pady=3, side="left")

for y in range(100, 600, 30):
    canvas.create_line(50, y, 900, y, tags=("label",))


def reset_wjs():
    reset()

rot.resizable(False, False)
rot.mainloop()