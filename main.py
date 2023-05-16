from tkinter import *
import tkinter.ttk


class MainGUI :
    def __init__(self) :
        window = Tk()
        window.title("노인통합 서비스")
        window.geometry("800x600")
        
        nb = tkinter.ttk.Notebook(window,width=800,height=600)
        nb.pack()
        
        framek = Frame(window) #요양시설 검색할 탭
        nb.add(framek,text='요양시설')
        frame2 = Frame(window) #전문병원 검색할 탭
        nb.add(frame2,text='전문병원')
        frame3 = Frame(window) #여가복지시설(경로당) 검색 탭
        nb.add(frame3,text='여가복지시설')
        
        window.mainloop()


MainGUI()