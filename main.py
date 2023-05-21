from tkinter import *
import requests
import tkinter.ttk
import json

key = 'fc79933d2b8f4ef3bdb6190a73ae8314'

class MainGUI:
    def search(self, tab_index):
        search_query = self.entrylist[tab_index].get()
        self.search_results = []  # 검색 결과 초기화

        if tab_index == 0:
            # 요양시설 검색
            url = f'https://openapi.gg.go.kr/OldPersonRecuperationFacility'
            params = {'KEY' : key,'Type' : 'xml', 'pIndex' : 1, 'pSize' : 100, 'SIGUN_NM': search_query}
            response = requests.get(url, params=params)
            
            self.lboxlist[tab_index].insert(END,response.text)

        elif tab_index == 1:
            # 전문병원 검색
            url = f'https://openapi.gg.go.kr/OldPersonSpecialityHospital'
            params = {'KEY' : key,'Type' : 'xml', 'pIndex' : 1, 'pSize' : 100, 'SIGUN_NM': search_query}
            response = requests.get(url, params=params)
            #data = json.loads(response.text)

            # # 검색 결과를 self.search_results에 저장
            # self.search_results = []
            # if 'row' in data:
            #     self.search_results = [
            #         f"{item['HOSPTL_NM']}, {item['TREAT_SBJECT_CNT']}"
            #         for item in data['row']
            #     ]
            # else:
            #     self.search_results = ['검색 결과가 없습니다.']

            # # 검색 결과를 리스트 박스에 추가
            # result_list = Listbox(self.framelist[tab_index], width=60, height=20)
            # result_list.place(x=0, y=200)

            # for result in self.search_results:
            #     result_list.insert(END, result)
            self.lboxlist[tab_index].insert(END,response.text)
        
        elif tab_index == 2:
            # 여가복지시설 검색
            url = f''
            params = {'SIGUN_NM': search_query}
            response = requests.get(url)

        elif tab_index == 3:
            # 의료복지시설 검색
            url = f''
            params = {'SIGUN_NM': search_query}
            response = requests.get(url)

        elif tab_index == 4:
            # 일자리지원기관 검색
            url = f''
            params = {'SIGUN_NM': search_query}
            response = requests.get(url)

        elif tab_index == 5:
            # 주거복지시설 검색
            url = f''
            params = {'SIGUN_NM': search_query}
            response = requests.get(url)

    def __init__(self):
        window = Tk()
        window.title("노인통합 서비스")
        window.geometry("800x600")

        nb = tkinter.ttk.Notebook(window, width=800, height=600)
        nb.pack()

        self.framelist = []

        for _ in range(7):
            self.framelist.append(Frame(window))

        nb.add(self.framelist[0], text='요양시설')
        nb.add(self.framelist[1], text='전문병원')
        nb.add(self.framelist[2], text='여가복지시설')
        nb.add(self.framelist[3], text='의료복지시설')
        nb.add(self.framelist[4], text='일자리지원기관')
        nb.add(self.framelist[5], text='주거복지시설')
        nb.add(self.framelist[6], text='즐겨찾기')

        Button(self.framelist[0], text='검색', command=lambda: self.search(0)).place(x=150, y=10)
        Button(self.framelist[1], text='검색', command=lambda: self.search(1)).place(x=150, y=10)
        Button(self.framelist[2], text='검색', command=lambda: self.search(2)).place(x=150, y=10)
        Button(self.framelist[3], text='검색', command=lambda: self.search(3)).place(x=150, y=10)
        Button(self.framelist[4], text='검색', command=lambda: self.search(4)).place(x=150, y=10)
        Button(self.framelist[5], text='검색', command=lambda: self.search(5)).place(x=150, y=10)
        Button(self.framelist[6], text='검색', command=lambda: self.search(6)).place(x=150, y=10)
        
        self.entrylist = []
        self.lboxlist = [] #리스트 박스가 담길 리스트

        for i in range(7):
            self.entrylist.append(Entry(self.framelist[i], width=19))
            self.entrylist[i].place(x=10, y=10)
            
            self.lboxlist.append(Listbox(self.framelist[i],width=60,height=10))
            self.lboxlist[i].place(x=5,y=80)

        window.mainloop()


MainGUI()