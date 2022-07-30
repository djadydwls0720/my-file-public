import sys
from tkinter import Frame
from musiclistvarcopy3 import Ui_MainWindow
from musiclist_addMusic import Ui_MainWindow as Ui_addmusicWindow
from PyQt5 import *
from PyQt5.QtCore import*
from PyQt5.QtWidgets import *
import webbrowser
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import QCoreApplication
from tkinter import*
import tkinter
import time

name1_lists=[]
name2_lists=[]
name3_lists=[]

music1_links=[]
music2_links=[]
music3_links=[]


with open("C:\\jaim\\musiclist1.txt","r", encoding="utf8") as f:
    for i in range(0, 36):
        music1_links.append(f.readline())
        
with open("C:\\jaim\\musiclist2.txt","r", encoding="utf8") as f:
    for i in range(0, 36):
        music2_links.append(f.readline())
        
with open("C:\\jaim\\musiclist3.txt","r", encoding="utf8") as f:
    for i in range(0, 36):
        music3_links.append(f.readline())
        
with open("C:\\jaim\\namelist1.txt","r", encoding="utf8") as f:
    for i in range(0, 36):
        name1_lists.append(f.readline())
                
with open("C:\\jaim\\namelist2.txt","r", encoding="utf8") as f:
    for i in range(0, 36):
        name2_lists.append(f.readline())
                
with open("C:\\jaim\\namelist3.txt","r", encoding="utf8") as f:
    for i in range(0, 36):
        name3_lists.append(f.readline())
        


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.show()
        self.page=1
        self.ok=True
        
        self.pushButton_78.setText(name1_lists[0].rstrip("\n"))
        self.pushButton_97.setText(name1_lists[1].rstrip("\n"))
        self.pushButton_79.setText(name1_lists[2].rstrip("\n"))
        self.pushButton_76.setText(name1_lists[3].rstrip("\n"))
        self.pushButton_83.setText(name1_lists[4].rstrip("\n"))
        self.pushButton_73.setText(name1_lists[5].rstrip("\n"))
        self.pushButton_99.setText(name1_lists[6].rstrip("\n"))
        self.pushButton_104.setText(name1_lists[7].rstrip("\n"))
        self.pushButton_98.setText(name1_lists[8].rstrip("\n"))
        self.pushButton_103.setText(name1_lists[9].rstrip("\n"))
        self.pushButton_92.setText(name1_lists[10].rstrip("\n"))
        self.pushButton_84.setText(name1_lists[11].rstrip("\n"))
        self.pushButton_95.setText(name1_lists[12].rstrip("\n"))
        self.pushButton_75.setText(name1_lists[13].rstrip("\n"))
        self.pushButton_100.setText(name1_lists[14].rstrip("\n"))
        self.pushButton_106.setText(name1_lists[15].rstrip("\n"))
        self.pushButton_86.setText(name1_lists[16].rstrip("\n"))
        self.pushButton_74.setText(name1_lists[17].rstrip("\n"))
        self.pushButton_107.setText(name1_lists[18].rstrip("\n"))
        self.pushButton_105.setText(name1_lists[19].rstrip("\n"))
        self.pushButton_89.setText(name1_lists[20].rstrip("\n"))
        self.pushButton_91.setText(name1_lists[21].rstrip("\n"))
        self.pushButton_80.setText(name1_lists[22].rstrip("\n"))
        self.pushButton_94.setText(name1_lists[23].rstrip("\n"))
        self.pushButton_101.setText(name1_lists[24].rstrip("\n"))
        self.pushButton_77.setText(name1_lists[25].rstrip("\n"))
        self.pushButton_88.setText(name1_lists[26].rstrip("\n"))
        self.pushButton_82.setText(name1_lists[27].rstrip("\n"))
        self.pushButton_90.setText(name1_lists[28].rstrip("\n"))
        self.pushButton_85.setText(name1_lists[29].rstrip("\n"))
        self.pushButton_87.setText(name1_lists[30].rstrip("\n"))
        self.pushButton_81.setText(name1_lists[31].rstrip("\n"))
        self.pushButton_93.setText(name1_lists[32].rstrip("\n"))
        self.pushButton_102.setText(name1_lists[33].rstrip("\n"))
        self.pushButton_96.setText(name1_lists[34].rstrip("\n"))
        
        

    def search(self):
        brwser=webdriver.Chrome()
        if self.radioButton.isChecked():
            brwser.get("https://www.naver.com/")
            brwser.find_element_by_xpath("//*[@id='query']").send_keys(str(self.search_text.text()))
            brwser.find_element_by_xpath("//*[@id='search_btn']").click()
        else:
            brwser.get("https://www.google.com/")
            brwser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(str(self.search_text.text()))
            brwser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()

    
    def search_youtube(self):
        brwser=webdriver.Chrome()
        brwser.get("https://www.youtube.com/")
        brwser.find_element_by_id("search").send_keys(str(self.search_text_yotude.text()))
        brwser.find_element_by_xpath("//*[@id='search-icon-legacy']").click()

    
    def clicked_Button0(self):
        pass
    
    def remocon(self):
        pass
    
    def corona19(self):
        url="http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun="
        res=requests.get(url)
        res.raise_for_status()
        soup=BeautifulSoup(res.text, "lxml")
        su=soup.find_all("p", attrs={"class":"inner_value"})

        QMessageBox.information(self,"알림", "국내 확진자:"+str(su[1].get_text())+"\n해외 유입:"+str(su[2].get_text())+"\n총합:"+str((su[0].get_text().replace("+ ", ""))))

    
    def wether(self):
        url="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hSXApwp0YihssiXI7usssssst3K-420576"
        url2="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80"

        url3="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%84%9C%EC%9A%B8%EC%B4%88%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80"

        res2=requests.get(url2)
        res2.raise_for_status()
        soup2=BeautifulSoup(res2.text, "lxml")

        res3=requests.get(url3)
        res3.raise_for_status()
        soup3=BeautifulSoup(res3.text, "lxml")

        res=requests.get(url)
        res.raise_for_status()
        soup=BeautifulSoup(res.text, "lxml")
        
        dhseh_list=soup.find_all("span",attrs={"class":"lowest"})
        dhseh2_list=soup.find_all("span",attrs={"class":"highest"})

      
        skfTL_list=soup.find_all("div",attrs={"class":"temperature_text"})
       

        altpajswl_list=soup2.find_all("span",attrs={"class":"value"})
        chaltpajswl_list=soup3.find_all("span",attrs={"class":"value"})
 

        rain_list=soup.find_all("dd",attrs={"class":"desc"})
        weher=soup.find_all("span",attrs={"class":"weather before_slash"})
  


        if(int(chaltpajswl_list[12].get_text())<15):
            a="좋음"
        
        elif(int(chaltpajswl_list[12].get_text())>15 & int(chaltpajswl_list[17].get_text())<35):
            a="보통"
            
        elif(int(chaltpajswl_list[12].get_text())>35 & int(chaltpajswl_list[17].get_text())<75):
            a="나쁨"
            
        elif(int(chaltpajswl_list[12].get_text())>76):
            a="매우나쁨"


        QMessageBox.information(self,"오늘 날씨", "현재온도:"+ str(skfTL_list[0].get_text().replace("현재 온도", "").replace("°", ""))+"℃"+" / "+str(weher[0].get_text())+"\n\n"+"최저기온: "+str(dhseh_list[0].get_text().replace("최저기온", "").replace("°", ""))+"℃"+"  "+"최고기온: "+str(dhseh2_list[0].get_text().replace("최고기온", "").replace("°", ""))+"℃"+"\n"+"강수확률: "+str(rain_list[0].get_text())+"  습도: "+str(rain_list[1].get_text())+"\n"+"미세먼지: "+str(altpajswl_list[0].get_text())+"㎍/㎥ / "+str(altpajswl_list[17].get_text())+"\n"+"초미세먼지: "+str(chaltpajswl_list[12].get_text())+"㎍/㎥ / "+str(a))

        url4="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EC%98%A4%EC%A0%84+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&tqi=hSXAwwp0J1ZsskiwShhssssssWR-122981"

        res4=requests.get(url4)
        res4.raise_for_status()
        soup4=BeautifulSoup(res4.text, "lxml")

        sodlfwether_list=soup4.find_all("p",attrs={"class":"summary"})

        QMessageBox.information(self, "내일 날씨", "오전:"+str(skfTL_list[1].get_text().replace("예측 온도", "").replace("°", ""))+"℃ / "+str(sodlfwether_list[1].get_text())+"\n"+"오후:"+str(skfTL_list[2].get_text().replace("예측 온도", "").replace("°", ""))+"℃ / "+str(sodlfwether_list[3].get_text()))
        # #4,5,6
    
    def thre(self):

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
            text=txt.get(1.0, tkinter.END)
            x=-5
            for i in range(0, 11):
                lis=eval(text)
                list_box.insert(i, str(x)+","+str(lis))
                x+=1

        def draw():
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
            
    def next(self):
        self.page+=1

        if self.page>3:
            self.page=3
        self.label_3.setText(str(self.page)+"/3")
        self.wjdfuf()
        

    def wjdfuf(self):
        if self.page==1:
            self.pushButton_78.setText(name1_lists[0].rstrip("\n"))
            self.pushButton_97.setText(name1_lists[1].rstrip("\n"))
            self.pushButton_79.setText(name1_lists[2].rstrip("\n"))
            self.pushButton_76.setText(name1_lists[3].rstrip("\n"))
            self.pushButton_83.setText(name1_lists[4].rstrip("\n"))

            self.pushButton_73.setText(name1_lists[5].rstrip("\n"))
            self.pushButton_99.setText(name1_lists[6].rstrip("\n"))
            self.pushButton_104.setText(name1_lists[7].rstrip("\n"))
            self.pushButton_98.setText(name1_lists[8].rstrip("\n"))

            self.pushButton_103.setText(name1_lists[9].rstrip("\n"))

            self.pushButton_92.setText(name1_lists[10].rstrip("\n"))
            self.pushButton_84.setText(name1_lists[11].rstrip("\n"))
            self.pushButton_95.setText(name1_lists[12].rstrip("\n"))
            self.pushButton_75.setText(name1_lists[13].rstrip("\n"))
            self.pushButton_100.setText(name1_lists[14].rstrip("\n"))

            self.pushButton_106.setText(name1_lists[15].rstrip("\n"))
            self.pushButton_86.setText(name1_lists[16].rstrip("\n"))
            self.pushButton_74.setText(name1_lists[17].rstrip("\n"))
            self.pushButton_107.setText(name1_lists[18].rstrip("\n"))
            self.pushButton_105.setText(name1_lists[19].rstrip("\n"))

            self.pushButton_89.setText(name1_lists[20].rstrip("\n"))
            self.pushButton_91.setText(name1_lists[21].rstrip("\n"))
            self.pushButton_80.setText(name1_lists[22].rstrip("\n"))
            self.pushButton_94.setText(name1_lists[23].rstrip("\n"))
            self.pushButton_101.setText(name1_lists[24].rstrip("\n"))

            self.pushButton_77.setText(name1_lists[25].rstrip("\n"))
            self.pushButton_88.setText(name1_lists[26].rstrip("\n"))

            self.pushButton_82.setText(name1_lists[27].rstrip("\n"))

            self.pushButton_90.setText(name1_lists[28].rstrip("\n"))
            self.pushButton_85.setText(name1_lists[29].rstrip("\n"))
            
            self.pushButton_87.setText(name1_lists[30].rstrip("\n"))
            self.pushButton_81.setText(name1_lists[31].rstrip("\n"))
            self.pushButton_93.setText(name1_lists[32].rstrip("\n"))
            self.pushButton_102.setText(name1_lists[33].rstrip("\n"))
            self.pushButton_96.setText(name1_lists[34].rstrip("\n"))
                
        if self.page==2:
            
            self.pushButton_78.setText(name2_lists[0].rstrip("\n"))
            self.pushButton_97.setText(name2_lists[1].rstrip("\n"))
            self.pushButton_79.setText(name2_lists[2].rstrip("\n"))
            self.pushButton_76.setText(name2_lists[3].rstrip("\n"))
            self.pushButton_83.setText(name2_lists[4].rstrip("\n"))
            self.pushButton_73.setText(name2_lists[5].rstrip("\n"))
            self.pushButton_99.setText(name2_lists[6].rstrip("\n"))
            self.pushButton_104.setText(name2_lists[7].rstrip("\n"))
            self.pushButton_98.setText(name2_lists[8].rstrip("\n"))

            self.pushButton_103.setText(name2_lists[9].rstrip("\n"))
            self.pushButton_92.setText(name2_lists[10].rstrip("\n"))
            self.pushButton_84.setText(name2_lists[11].rstrip("\n"))
            self.pushButton_95.setText(name2_lists[12].rstrip("\n"))
            self.pushButton_75.setText(name2_lists[13].rstrip("\n"))
            self.pushButton_100.setText(name2_lists[14].rstrip("\n"))
            self.pushButton_106.setText(name2_lists[15].rstrip("\n"))
            self.pushButton_86.setText(name2_lists[16].rstrip("\n"))
            self.pushButton_74.setText(name2_lists[17].rstrip("\n"))
            self.pushButton_107.setText(name2_lists[18].rstrip("\n"))
            self.pushButton_105.setText(name2_lists[19].rstrip("\n"))
            self.pushButton_89.setText(name2_lists[20].rstrip("\n"))
            self.pushButton_91.setText(name2_lists[21].rstrip("\n"))
            self.pushButton_80.setText(name2_lists[22].rstrip("\n"))
            self.pushButton_94.setText(name2_lists[23].rstrip("\n"))
            self.pushButton_101.setText(name2_lists[24].rstrip("\n"))
            self.pushButton_77.setText(name2_lists[25].rstrip("\n"))
            self.pushButton_88.setText(name2_lists[26].rstrip("\n"))

            self.pushButton_82.setText(name2_lists[27].rstrip("\n"))

            self.pushButton_90.setText(name2_lists[28].rstrip("\n"))
            self.pushButton_85.setText(name2_lists[29].rstrip("\n"))
            self.pushButton_87.setText(name2_lists[30].rstrip("\n"))
            self.pushButton_81.setText(name2_lists[31].rstrip("\n"))
            self.pushButton_93.setText(name2_lists[32].rstrip("\n"))
            self.pushButton_102.setText(name2_lists[33].rstrip("\n"))
            self.pushButton_96.setText(name2_lists[34].rstrip("\n"))
                    
        if self.page==3:
                
            self.pushButton_78.setText(name3_lists[0].rstrip("\n"))
            self.pushButton_97.setText(name3_lists[1].rstrip("\n"))
            self.pushButton_79.setText(name3_lists[2].rstrip("\n"))
            self.pushButton_76.setText(name3_lists[3].rstrip("\n"))
            self.pushButton_83.setText(name3_lists[4].rstrip("\n"))
            self.pushButton_73.setText(name3_lists[5].rstrip("\n"))
            self.pushButton_99.setText(name3_lists[6].rstrip("\n"))
            self.pushButton_104.setText(name3_lists[7].rstrip("\n"))
            self.pushButton_98.setText(name3_lists[8].rstrip("\n"))

            self.pushButton_103.setText(name3_lists[9].rstrip("\n"))
            self.pushButton_92.setText(name3_lists[10].rstrip("\n"))
            self.pushButton_84.setText(name3_lists[11].rstrip("\n"))
            self.pushButton_95.setText(name3_lists[12].rstrip("\n"))
            self.pushButton_75.setText(name3_lists[13].rstrip("\n"))
            self.pushButton_100.setText(name3_lists[14].rstrip("\n"))
            self.pushButton_106.setText(name3_lists[15].rstrip("\n"))
            self.pushButton_86.setText(name3_lists[16].rstrip("\n"))
            self.pushButton_74.setText(name3_lists[17].rstrip("\n"))
            self.pushButton_107.setText(name3_lists[18].rstrip("\n"))
            self.pushButton_105.setText(name3_lists[19].rstrip("\n"))
            self.pushButton_89.setText(name3_lists[20].rstrip("\n"))
            self.pushButton_91.setText(name3_lists[21].rstrip("\n"))
            self.pushButton_80.setText(name3_lists[22].rstrip("\n"))
            self.pushButton_94.setText(name3_lists[23].rstrip("\n"))
            self.pushButton_101.setText(name3_lists[24].rstrip("\n"))
            self.pushButton_77.setText(name3_lists[25].rstrip("\n"))
            self.pushButton_88.setText(name3_lists[26].rstrip("\n"))

            self.pushButton_82.setText(name3_lists[27].rstrip("\n"))

            self.pushButton_90.setText(name3_lists[28].rstrip("\n"))
            self.pushButton_85.setText(name3_lists[29].rstrip("\n"))
            self.pushButton_87.setText(name3_lists[30].rstrip("\n"))
            self.pushButton_81.setText(name3_lists[31].rstrip("\n"))
            self.pushButton_93.setText(name3_lists[32].rstrip("\n"))
            self.pushButton_102.setText(name3_lists[33].rstrip("\n"))
            self.pushButton_96.setText(name3_lists[34].rstrip("\n"))
    def back(self):
        self.page-=1

        if self.page<1:
            self.page=1
        
        self.label_3.setText(str(self.page)+"/3")
        self.wjdfuf()

       
    
    def dele(self):
        global name1_lists,name2_lists,name3_lists,music1_links,music2_links,music3_links

        if self.page==1:
            with open("C:\\jaim\\musiclist1.txt","w", encoding="utf8") as f:
                music1_links=[]

                for i in range(0, 36):
                    music1_links.append("")

            with open("C:\\jaim\\namelist1.txt","w", encoding="utf8") as f:
                name1_lists=[]

                for i in range(0, 36):
                    name1_lists.append("")
                    
        if self.page==2:
            with open("C:\\jaim\\namelist2.txt","w", encoding="utf8") as f:
                name2_lists=[]

                for i in range(0, 36):
                    name2_lists.append("")
                    
            with open("C:\\jaim\\musiclist2.txt","w", encoding="utf8") as f:
                music2_links=[]
                
                for i in range(0,36):
                    music2_links.append("")
                
        
        if self.page==3:              
            with open("C:\\jaim\\namelist3.txt","w", encoding="utf8") as f:
                name3_lists=[]

                for i in range(0, 36):
                    name3_lists.append("")
                            
            with open("C:\\jaim\\musiclist3.txt","w", encoding="utf8") as f:
                music3_links=[]

                for i in range(0, 36):
                    music3_links.append("")
        self.wjdfuf()
        

    def deleend():
        pass



    def addmusic(self,Button,number):
        self.a=addMusicWindow(self.page,Button,number)
        

            
    
    def click_btn0(self):
        if self.page==1:
            if name1_lists[0]=="":
                self.addmusic(self.pushButton_78,0)
            else:
                webbrowser.open(music1_links[0])
    
        if self.page==2:
            if name2_lists[0]=="":
                self.addmusic(self.pushButton_78,0)
            else:
                webbrowser.open(music2_links[0])

        if self.page==3:
            if name3_lists[0]=="":
                self.addmusic(self.pushButton_78,0)
            else:
                webbrowser.open(music3_links[0])



    def click_btn1(self):
        if self.page==1:
            if name1_lists[1]=="":
                self.addmusic(self.pushButton_97,1)
            else:
                webbrowser.open(music1_links[1])
    
        if self.page==2:
            if name2_lists[1]=="":
                self.addmusic(self.pushButton_97,1)
            else:
                webbrowser.open(music2_links[1])

        if self.page==3:
            if name3_lists[1]=="":
                self.addmusic(self.pushButton_97,1)
            else:
                webbrowser.open(music3_links[1])
    
    def click_btn2(self):
        if self.page==1:
            if name1_lists[2]=="":
                self.addmusic(self.pushButton_79,2)
            else:
                webbrowser.open(music1_links[2])
    
        if self.page==2:
            if name2_lists[2]=="":
                self.addmusic(self.pushButton_79,2)
            else:
                webbrowser.open(music2_links[2])

        if self.page==3:
            if name3_lists[2]=="":
                self.addmusic(self.pushButton_79,2)
            else:
                webbrowser.open(music3_links[2])
    
    def click_btn3(self):
        if self.page==1:
            if name1_lists[3]=="":
                self.addmusic(self.pushButton_76,3)
            else:
                webbrowser.open(music1_links[3])
    
        if self.page==2:
            if name2_lists[3]=="":
                self.addmusic(self.pushButton_76,3)
            else:
                webbrowser.open(music2_links[3])

        if self.page==3:
            if name3_lists[3]=="":
                self.addmusic(self.pushButton_76,3)
            else:
                webbrowser.open(music3_links[3])
    
    def click_btn4(self):
        
        if self.page==1:
            if name1_lists[4]=="":
                self.addmusic(self.pushButton_83,4)
            else:
                webbrowser.open(music1_links[4])
    
        if self.page==2:
            if name2_lists[4]=="":
                self.addmusic(self.pushButton_83,4)
            else:
                webbrowser.open(music2_links[4])

        if self.page==3:
            if name3_lists[4]=="":
                self.addmusic(self.pushButton_83,4)
            else:
                webbrowser.open(music3_links[4])
    
    def click_btn5(self):
        
        if self.page==1:
            if name1_lists[5]=="":
                self.addmusic(self.pushButton_73,5)
            else:
                webbrowser.open(music1_links[5])
    
        if self.page==2:
            if name2_lists[5]=="":
                self.addmusic(self.pushButton_73,5)
            else:
                webbrowser.open(music2_links[5])

        if self.page==3:
            if name3_lists[5]=="":
                self.addmusic(self.pushButton_73,5)
            else:
                webbrowser.open(music3_links[5])
    
    def click_btn6(self):
        
        if self.page==1:
            if name1_lists[6]=="":
                self.addmusic(self.pushButton_99,6)
            else:
                webbrowser.open(music1_links[6])
    
        if self.page==2:
            if name2_lists[6]=="":
                self.addmusic(self.pushButton_99,6)
            else:
                webbrowser.open(music2_links[6])

        if self.page==3:
            if name3_lists[6]=="":
                self.addmusic(self.pushButton_99,6)
            else:
                webbrowser.open(music3_links[6])
    
    def click_btn7(self):
        
        if self.page==1:
            if name1_lists[7]=="":
                self.addmusic(self.pushButton_104,7)
            else:
                webbrowser.open(music1_links[7])
    
        if self.page==2:
            if name2_lists[7]=="":
                self.addmusic(self.pushButton_104,7)
            else:
                webbrowser.open(music2_links[7])

        if self.page==3:
            if name3_lists[7]=="":
                self.addmusic(self.pushButton_104,7)
            else:
                webbrowser.open(music3_links[7])
    
    def click_btn8(self):
        
        if self.page==1:
            if name1_lists[8]=="":
                self.addmusic(self.pushButton_98,8)
            else:
                webbrowser.open(music1_links[8])
    
        if self.page==2:
            if name2_lists[8]=="":
                self.addmusic(self.pushButton_98,8)
            else:
                webbrowser.open(music2_links[8])

        if self.page==3:
            if name3_lists[8]=="":
                self.addmusic(self.pushButton_98,8)
            else:
                webbrowser.open(music3_links[8])
    
    def click_btn9(self):
        
        if self.page==1:
            if name1_lists[9]=="":
                self.addmusic(self.pushButton_103,9)
            else:
                webbrowser.open(music1_links[9])
    
        if self.page==2:
            if name2_lists[9]=="":
                self.addmusic(self.pushButton_103,9)
            else:
                webbrowser.open(music2_links[9])

        if self.page==3:
            if name3_lists[9]=="":
                self.addmusic(self.pushButton_103,9)
            else:
                webbrowser.open(music3_links[9])
    
    def click_btn10(self):
        
        if self.page==1:
            if name1_lists[10]=="":
                self.addmusic(self.pushButton_92,10)
            else:
                webbrowser.open(music1_links[10])
    
        if self.page==2:
            if name2_lists[10]=="":
                self.addmusic(self.pushButton_92,10)
            else:
                webbrowser.open(music2_links[10])

        if self.page==3:
            if name3_lists[10]=="":
                self.addmusic(self.pushButton_92,10)
            else:
                webbrowser.open(music3_links[10])
    
    def click_btn11(self):
        
        if self.page==1:
            if name1_lists[11]=="":
                self.addmusic(self.pushButton_84,11)
            else:
                webbrowser.open(music1_links[11])
    
        if self.page==2:
            if name2_lists[11]=="":
                self.addmusic(self.pushButton_84,11)
            else:
                webbrowser.open(music2_links[11])

        if self.page==3:
            if name3_lists[11]=="":
                self.addmusic(self.pushButton_84,11)
            else:
                webbrowser.open(music3_links[11])
    
    def click_btn12(self):
        
        if self.page==1:
            if name1_lists[12]=="":
                self.addmusic(self.pushButton_95,12)
            else:
                webbrowser.open(music1_links[12])
    
        if self.page==2:
            if name2_lists[12]=="":
                self.addmusic(self.pushButton_95,12)
            else:
                webbrowser.open(music2_links[12])

        if self.page==3:
            if name3_lists[12]=="":
                self.addmusic(self.pushButton_95,12)
            else:
                webbrowser.open(music3_links[12])
    
    def click_btn13(self):
        
        if self.page==1:
            if name1_lists[13]=="":
                self.addmusic(self.pushButton_75,13)
            else:
                webbrowser.open(music1_links[13])
    
        if self.page==2:
            if name2_lists[13]=="":
                self.addmusic(self.pushButton_75,13)
            else:
                webbrowser.open(music2_links[13])

        if self.page==3:
            if name3_lists[13]=="":
                self.addmusic(self.pushButton_75,13)
            else:
                webbrowser.open(music3_links[13])
    
    def click_btn14(self):
        
        if self.page==1:
            if name1_lists[14]=="":
                self.addmusic(self.pushButton_100,14)
            else:
                webbrowser.open(music1_links[14])
    
        if self.page==2:
            if name2_lists[14]=="":
                self.addmusic(self.pushButton_100,14)
            else:
                webbrowser.open(music2_links[14])

        if self.page==3:
            if name3_lists[14]=="":
                self.addmusic(self.pushButton_100,14)
            else:
                webbrowser.open(music3_links[14])
    
    def click_btn15(self):
        
        if self.page==1:
            if name1_lists[15]=="":
                self.addmusic(self.pushButton_106,15)
            else:
                webbrowser.open(music1_links[15])
    
        if self.page==2:
            if name2_lists[15]=="":
                self.addmusic(self.pushButton_106,15)
            else:
                webbrowser.open(music2_links[15])

        if self.page==3:
            if name3_lists[15]=="":
                self.addmusic(self.pushButton_106,15)
            else:
                webbrowser.open(music3_links[15])
    
    def click_btn16(self):
        
        if self.page==1:
            if name1_lists[16]=="":
                self.addmusic(self.pushButton_86,16)
            else:
                webbrowser.open(music1_links[16])
    
        if self.page==2:
            if name2_lists[16]=="":
                self.addmusic(self.pushButton_86,16)
            else:
                webbrowser.open(music2_links[16])

        if self.page==3:
            if name3_lists[16]=="":
                self.addmusic(self.pushButton_86,16)
            else:
                webbrowser.open(music3_links[16])
    
    def click_btn17(self):
        
        if self.page==1:
            if name1_lists[17]=="":
                self.addmusic(self.pushButton_74,17)
            else:
                webbrowser.open(music1_links[17])
    
        if self.page==2:
            if name2_lists[17]=="":
                self.addmusic(self.pushButton_74,17)
            else:
                webbrowser.open(music2_links[17])

        if self.page==3:
            if name3_lists[17]=="":
                self.addmusic(self.pushButton_74,17)
            else:
                webbrowser.open(music3_links[17])
    
    def click_btn18(self):
        
        if self.page==1:
            if name1_lists[18]=="":
                self.addmusic(self.pushButton_107,18)
            else:
                webbrowser.open(music1_links[18])
    
        if self.page==2:
            if name2_lists[18]=="":
                self.addmusic(self.pushButton_107,18)
            else:
                webbrowser.open(music2_links[18])

        if self.page==3:
            if name3_lists[18]=="":
                self.addmusic(self.pushButton_107,18)
            else:
                webbrowser.open(music3_links[18])
    
    def click_btn19(self):
        
        if self.page==1:
            if name1_lists[19]=="":
                self.addmusic(self.pushButton_105,19)
            else:
                webbrowser.open(music1_links[19])
    
        if self.page==2:
            if name2_lists[19]=="":
                self.addmusic(self.pushButton_105,19)
            else:
                webbrowser.open(music2_links[19])

        if self.page==3:
            if name3_lists[19]=="":
                self.addmusic(self.pushButton_105,19)
            else:
                webbrowser.open(music3_links[19])
    
    def click_btn20(self):
        
        if self.page==1:
            if name1_lists[20]=="":
                self.addmusic(self.pushButton_89,20)
            else:
                webbrowser.open(music1_links[20])
    
        if self.page==2:
            if name2_lists[20]=="":
                self.addmusic(self.pushButton_89,20)
            else:
                webbrowser.open(music2_links[20])

        if self.page==3:
            if name3_lists[20]=="":
                self.addmusic(self.pushButton_89,20)
            else:
                webbrowser.open(music3_links[20])
    
    def click_btn21(self):
        
        if self.page==1:
            if name1_lists[21]=="":
                self.addmusic(self.pushButton_91,21)
            else:
                webbrowser.open(music1_links[21])
    
        if self.page==2:
            if name2_lists[21]=="":
                self.addmusic(self.pushButton_91,21)
            else:
                webbrowser.open(music2_links[21])

        if self.page==3:
            if name3_lists[21]=="":
                self.addmusic(self.pushButton_91,21)
            else:
                webbrowser.open(music3_links[21])
    
    def click_btn22(self):
        
        if self.page==1:
            if name1_lists[22]=="":
                self.addmusic(self.pushButton_80,22)
            else:
                webbrowser.open(music1_links[22])
    
        if self.page==2:
            if name2_lists[22]=="":
                self.addmusic(self.pushButton_80,22)
            else:
                webbrowser.open(music2_links[22])

        if self.page==3:
            if name3_lists[22]=="":
                self.addmusic(self.pushButton_80,22)
            else:
                webbrowser.open(music3_links[22])
    
    def click_btn23(self):
        
        if self.page==1:
            if name1_lists[23]=="":
                self.addmusic(self.pushButton_94,23)
            else:
                webbrowser.open(music1_links[23])
    
        if self.page==2:
            if name2_lists[23]=="":
                self.addmusic(self.pushButton_94,23)
            else:
                webbrowser.open(music2_links[23])

        if self.page==3:
            if name3_lists[23]=="":
                self.addmusic(self.pushButton_94,23)
            else:
                webbrowser.open(music3_links[23])
    
    def click_btn24(self):
        
        if self.page==1:
            if name1_lists[24]=="":
                self.addmusic(self.pushButton_101,24)
            else:
                webbrowser.open(music1_links[24])
    
        if self.page==2:
            if name2_lists[24]=="":
                self.addmusic(self.pushButton_101,24)
            else:
                webbrowser.open(music2_links[24])

        if self.page==3:
            if name3_lists[24]=="":
                self.addmusic(self.pushButton_101,24)
            else:
                webbrowser.open(music3_links[24])
    
    def click_btn25(self):
        
        if self.page==1:
            if name1_lists[25]=="":
                self.addmusic(self.pushButton_77,25)
            else:
                webbrowser.open(music1_links[25])
    
        if self.page==2:
            if name2_lists[25]=="":
                self.addmusic(self.pushButton_77,25)
            else:
                webbrowser.open(music2_links[25])

        if self.page==3:
            if name3_lists[25]=="":
                self.addmusic(self.pushButton_77,25)
            else:
                webbrowser.open(music3_links[25])
    
    def click_btn26(self):
        
        if self.page==1:
            if name1_lists[26]=="":
                self.addmusic(self.pushButton_88,26)
            else:
                webbrowser.open(music1_links[26])
    
        if self.page==2:
            if name2_lists[26]=="":
                self.addmusic(self.pushButton_88,26)
            else:
                webbrowser.open(music2_links[26])

        if self.page==3:
            if name3_lists[26]=="":
                self.addmusic(self.pushButton_88,26)
            else:
                webbrowser.open(music3_links[26])
    
    def click_btn27(self):
        
        if self.page==1:
            if name1_lists[27]=="":
                self.addmusic(self.pushButton_82,27)
            else:
                webbrowser.open(music1_links[27])
    
        if self.page==2:
            if name2_lists[27]=="":
                self.addmusic(self.pushButton_82,27)
            else:
                webbrowser.open(music2_links[27])

        if self.page==3:
            if name3_lists[27]=="":
                self.addmusic(self.pushButton_82,27)
            else:
                webbrowser.open(music3_links[27])
    
    def click_btn28(self):
        
        if self.page==1:
            if name1_lists[28]=="":
                self.addmusic(self.pushButton_90,28)
            else:
                webbrowser.open(music1_links[28])
    
        if self.page==2:
            if name2_lists[28]=="":
                self.addmusic(self.pushButton_90,28)
            else:
                webbrowser.open(music2_links[28])

        if self.page==3:
            if name3_lists[28]=="":
                self.addmusic(self.pushButton_90,28)
            else:
                webbrowser.open(music3_links[28])
    
    def click_btn29(self):
        
        if self.page==1:
            if name1_lists[29]=="":
                self.addmusic(self.pushButton_85,29)
            else:
                webbrowser.open(music1_links[29])
    
        if self.page==2:
            if name2_lists[29]=="":
                self.addmusic(self.pushButton_85,29)
            else:
                webbrowser.open(music2_links[29])

        if self.page==3:
            if name3_lists[29]=="":
                self.addmusic(self.pushButton_85,29)
            else:
                webbrowser.open(music3_links[29])
    
    def click_btn30(self):
        
        if self.page==1:
            if name1_lists[30]=="":
                self.addmusic(self.pushButton_87,30)
            else:
                webbrowser.open(music1_links[30])
    
        if self.page==2:
            if name2_lists[30]=="":
                self.addmusic(self.pushButton_87,30)
            else:
                webbrowser.open(music2_links[30])

        if self.page==3:
            if name3_lists[30]=="":
                self.addmusic(self.pushButton_87,30)
            else:
                webbrowser.open(music3_links[30])
    
    def click_btn31(self):
        
        if self.page==1:
            if name1_lists[31]=="":
                self.addmusic(self.pushButton_81,31)
            else:
                webbrowser.open(music1_links[31])
    
        if self.page==2:
            if name2_lists[31]=="":
                self.addmusic(self.pushButton_81,31)
            else:
                webbrowser.open(music2_links[31])

        if self.page==3:
            if name3_lists[31]=="":
                self.addmusic(self.pushButton_81,31)
            else:
                webbrowser.open(music3_links[31])
    

    def click_btn32(self):
        
        if self.page==1:
            if name1_lists[32]=="":
                self.addmusic(self.pushButton_93,32)
            else:
                webbrowser.open(music1_links[32])
    
        if self.page==2:
            if name2_lists[32]=="":
                self.addmusic(self.pushButton_93,32)
            else:
                webbrowser.open(music2_links[32])

        if self.page==3:
            if name3_lists[32]=="":
                self.addmusic(self.pushButton_93,32)
            else:
                webbrowser.open(music3_links[32])


    def click_btn33(self):
        
        if self.page==1:
            if name1_lists[33]=="":
                self.addmusic(self.pushButton_102,33)
            else:
                webbrowser.open(music1_links[33])
    
        if self.page==2:
            if name2_lists[33]=="":
                self.addmusic(self.pushButton_102,33)
            else:
                webbrowser.open(music2_links[33])

        if self.page==3:
            if name3_lists[33]=="":
                self.addmusic(self.pushButton_102,33)
            else:
                webbrowser.open(music3_links[33])
    
    def click_btn34(self):
        
        if self.page==1:
            if name1_lists[34]=="":
                self.addmusic(self.pushButton_96,34)
            else:
                webbrowser.open(music1_links[34])
    
        if self.page==2:
            if name2_lists[34]=="":
                self.addmusic(self.pushButton_96,34)
            else:
                webbrowser.open(music2_links[34])

        if self.page==3:
            if name3_lists[34]=="":
                self.addmusic(self.pushButton_96,34)
            else:
                webbrowser.open(music3_links[34])
    
    
        

class addMusicWindow(QMainWindow, Ui_addmusicWindow,Ui_MainWindow):
    def __init__(self, inpage,btn,number):
        super().__init__()
        self.inpage=inpage
        self.btn=btn
        self.number=number

        self.setupUi(self)
        self.show()

    def addmusicokay(self):
        if self.inpage==1:
            if str(self.lineEdit_2.text())=="":
                QMessageBox.information(self,"경고","링크를 안적었습니다!")
                
                return
            if str(self.lineEdit.text())=="":
                QMessageBox.information(self,"경고","제목을 안적었습니다!")
                return

            name1_lists[int(self.number)]=str(self.lineEdit.text())
            music1_links[int(self.number)]=str(self.lineEdit_2.text())

            with open("C:\\jaim\\namelist1.txt","a", encoding="utf8") as f:
                with open("C:\\jaim\\namelist1.txt","r", encoding="utf8") as fr:
                    if fr.readline()=="":
                        f.write(str(self.lineEdit.text()))

                            
                    else:f.write("\n"+str(self.lineEdit.text()))

            with open("C:\\jaim\\musiclist1.txt","a", encoding="utf8") as f:
                with open("C:\\jaim\\musiclist1.txt","r", encoding="utf8") as fr:
                    if fr.readline()=="":
                        f.write(str(self.lineEdit_2.text()))
                        
                    else:
                        f.write("\n"+str(self.lineEdit_2.text()))
                        

                

            self.btn.setText(str(self.lineEdit.text()))
            self.close()



        if self.inpage==2:
            if str(self.lineEdit_2.text())=="":
                QMessageBox.information(self,"경고","링크를 안적었습니다!")
                
                return
            if str(self.lineEdit.text())=="":
                QMessageBox.information(self,"경고","제목을 안적었습니다!")
                return

            name2_lists.insert(self.number, str(self.lineEdit.text()))
            music2_links.insert(self.number, str(self.lineEdit_2.text()))

            with open("C:\\jaim\\namelist2.txt","a", encoding="utf8") as f:
                with open("C:\\jaim\\namelist2.txt","r", encoding="utf8") as fr:
                    if fr.readline()=="":
                        f.write(str(self.lineEdit.text()))

                            
                    else:f.write("\n"+str(self.lineEdit.text()))

            with open("C:\\jaim\\musiclist2.txt","a", encoding="utf8") as f:
                with open("C:\\jaim\\musiclist2.txt","r", encoding="utf8") as fr:
                    if fr.readline()=="":
                        f.write(str(self.lineEdit_2.text()))
                        
                    else:
                        f.write("\n"+str(self.lineEdit_2.text()))
                        

            self.btn.setText(str(self.lineEdit.text()))
            self.close()



        if self.inpage==3:
            if str(self.lineEdit_2.text())=="":
                QMessageBox.information(self,"경고","링크를 안적었습니다!")
                
                return
            if str(self.lineEdit.text())=="":
                QMessageBox.information(self,"경고","제목을 안적었습니다!")
                return

            name3_lists.insert(self.number, str(self.lineEdit.text()))
            music3_links.insert(self.number, str(self.lineEdit_2.text()))

            with open("C:\\jaim\\namelist3.txt","a", encoding="utf8") as f:
                with open("C:\\jaim\\namelist3.txt","r", encoding="utf8") as fr:
                    if fr.readline()=="":
                        f.write(str(self.lineEdit.text()))

                            
                    else:f.write("\n"+str(self.lineEdit.text()))

            with open("C:\\jaim\\musiclist3.txt","a", encoding="utf8") as f:
                with open("C:\\jaim\\musiclist3.txt","r", encoding="utf8") as fr:
                    if fr.readline()=="":
                        f.write(str(self.lineEdit_2.text()))
                        
                    else:
                        f.write("\n"+str(self.lineEdit_2.text()))
                        

                

            self.btn.setText(str(self.lineEdit.text()))
            self.close()
          
    
    
app=QApplication([])
an=MainWindow()
QApplication.processEvents()
sys.exit(app.exec_())