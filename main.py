from tkinter import *
import tkinter.ttk


class MainGUI :
    def serch(self,page) :
        pass
    
    def __init__(self) :
        window = Tk()
        window.title("노인통합 서비스")
        window.geometry("800x600")
        
        nb = tkinter.ttk.Notebook(window,width=800,height=600)
        nb.pack()
        
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