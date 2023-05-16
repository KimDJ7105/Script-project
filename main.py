from tkinter import *
import tkinter.ttk


class MainGUI :
    def __init__(self) :
        window = Tk()
        window.title("노인통합 서비스")
        window.geometry("800x600")
        
        nb = tkinter.ttk.Notebook(window,width=800,height=600)
        nb.pack()
        
        self.frame1 = Frame(window) #요양시설 검색할 탭
        nb.add(self.frame1,text='요양시설')
        self.frame2 = Frame(window) #전문병원 검색할 탭
        nb.add(self.frame2,text='전문병원')
        self.frame3 = Frame(window) #여가복지시설(경로당) 검색 탭
        nb.add(self.frame3,text='여가복지시설')
        self.frame4 = Frame(window) #의료복지시설 검색 탭
        nb.add(self.frame4,text='의료복지시설')
        self.frame5 = Frame(window) #일자리지원기관 검색 탭
        nb.add(self.frame5,text='일자리지원기관')
        self.frame6 = Frame(window) #주거복지시설 검색 탭
        nb.add(self.frame6,text='주거복지시설')
        self.frame7 = Frame(window) #즐겨찾기 탭
        nb.add(self.frame7,text='즐겨찾기')
        
        self.e1 = Entry(self.frame1,width=19)
        self.e1.place(x=10, y=10)
        Button(self.frame1,text='검색').place(x=150,y=10)
        
        
        window.mainloop()


MainGUI()