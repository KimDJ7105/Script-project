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
        
        window.mainloop()


MainGUI()