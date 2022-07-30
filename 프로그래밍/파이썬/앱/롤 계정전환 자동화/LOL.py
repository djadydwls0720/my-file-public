from time import sleep
import pyautogui as py
from tkinter import *
import tkinter
import pyperclip as py2


KNG2021_id="djadydwls0720"
KNG2021_password="YONG0022"

SKNG2021_id="djadydwls7020"
SKNG2021_password="yong0021!"

def quit():
    i=py.locateCenterOnScreen("C:\\Users\\yongjin\\Desktop\\pyworkspace\\V11.png")
    if i!=None:
        py.click(i)
        py.hotkey("alt", "F4")
        i=py.locateCenterOnScreen("C:\\Users\\yongjin\\Desktop\\pyworkspace\\logout.png")
        py.click(i)
        return 0

    else:
        i=py.locateCenterOnScreen("C:\\Users\\yongjin\\Desktop\\pyworkspace\\LoL.png")
        py.click(i)
        py.hotkey("alt", "F4")
        i=py.locateCenterOnScreen("C:\\Users\\yongjin\\Desktop\\pyworkspace\\logout.png")
        py.click(i)
        return 0

def Login(ID, password):
    quit()
    while(1):
        py.sleep(0.1)
        i=py.locateCenterOnScreen("C:\\Users\\yongjin\\Desktop\\pyworkspace\\LOGIN3.png")
        if i!=None:
            i=py.locateCenterOnScreen("C:\\Users\\yongjin\\Desktop\\pyworkspace\\qlalfqjsgh.png")
            py.click(i)
            py2.copy(password)
            py.hotkey("ctrl", "v")
            i=py.locateCenterOnScreen("C:\\Users\\yongjin\\Desktop\\pyworkspace\\rPwjddlfma.png")
            py.click(i)
            py2.copy(ID)
            py.hotkey("ctrl", "v")
            i=py.locateCenterOnScreen("C:\\Users\\yongjin\\Desktop\\pyworkspace\\qlszks.png")
            py.click(i)
            i=py.locateCenterOnScreen("C:\\Users\\yongjin\\Desktop\\pyworkspace\\ekdma.png")
            py.click(i)
            while(1):    
                i=py.locateCenterOnScreen("C:\\Users\\yongjin\\Desktop\\pyworkspace\\PLAY.png")
                if i!=None:
                    py.click(i)
                    break
            break

def KNG2021():
    Login(KNG2021_id, KNG2021_password)



def SKNG2021():
    Login(SKNG2021_id, SKNG2021_password)

screen_x=150
screen_y=50
rot=Tk()
rot.title("")
rot.geometry(str(screen_x)+"x"+str(screen_y))

KNG2021_btn=Button(rot, text="KNG2021", padx=3, command=KNG2021)
KNG2021_btn.pack(side="left", padx=3)

SKNG2021_btn=Button(rot, text="SKNG2021", padx=3, command=SKNG2021)
SKNG2021_btn.pack(side="left", padx=3)


rot.resizable(False, False)
rot.mainloop()
