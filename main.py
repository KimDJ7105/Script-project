from tkinter import *
import tkinter.ttk


class MainGUI :
    def __init__(self) :
        window = Tk()
        window.title("노인통합 서비스")
        window.geometry("800x600")
        
        nb = tkinter.ttk.Notebook(window,width=800,height=600)
        nb.pack()
        
        frame1 = Frame(window) #요양시설 검색할 탭
        nb.add(frame1,text='요양시설')
        frame2 = Frame(window) #전문병원 검색할 탭
        nb.add(frame2,text='전문병원')
        frame3 = Frame(window) #여가복지시설(경로당) 검색 탭
        nb.add(frame3,text='여가복지시설')
        frame4 = Frame(window) #의료복지시설 검색 탭
        nb.add(frame4,text='의료복지시설')
        frame5 = Frame(window) #일자리지원기관 검색 탭
        nb.add(frame5,text='일자리지원기관')
        frame6 = Frame(window) #주거복지시설 검색 탭
        nb.add(frame6,text='주거복지시설')
        frame7 = Frame(window) #즐겨찾기 탭
        nb.add(frame7,text='즐겨찾기')
        
        window.mainloop()


MainGUI()