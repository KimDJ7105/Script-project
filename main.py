from tkinter import *
import tkinter.messagebox
import tkinter.ttk


class MainGUI :

    def searchButton(self):
        self.e = {}  # 딕셔너리를 초기화
        for i in range(1, 7):
            self.e[i] = Entry(self.frame[i], width=19)
            self.e[i].place(x=10, y=10)
            Button(self.frame[i], text='검색').place(x=150, y=10)

class MainGUI:
    def serch(self,page) :
        pass

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

        searchButton()

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
        self.framelist = []
        
        for _ in range(7) :
            self.framelist.append(Frame(window))
        
        nb.add(self.framelist[0],text='요양시설')
        nb.add(self.framelist[1],text='전문병원')
        nb.add(self.framelist[2],text='여가복지시설')
        nb.add(self.framelist[3],text='의료복지시설')
        nb.add(self.framelist[4],text='일자리지원기관')
        nb.add(self.framelist[5],text='주거복지시설')
        nb.add(self.framelist[6],text='즐겨찾기')

        self.entrylist = []
        
        for i in range(7) :
            self.entrylist.append(Entry(self.framelist[i],width=19))
            self.entrylist[i].place(x=10,y=10)
            
            Button(self.framelist[i], text='검색',command=lambda : self.serch(i)).place(x=150, y=10)
        
        #요양시설 탭에 필요한 구성품들
        
        hospital_list = Listbox(self.framelist[0], width=60,height=20)
        hospital_list.place(x=0,y=200)
        window.mainloop()


MainGUI()