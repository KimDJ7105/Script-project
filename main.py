from tkinter import *
import requests
import tkinter.ttk
import xml.etree.ElementTree as ET
import json

key = 'fc79933d2b8f4ef3bdb6190a73ae8314'

class MainGUI:
    def search(self, tab_index):
        search_query = self.entrylist[tab_index].get()
        self.search_results = []  # 검색 결과 초기화
        root = NONE

        if tab_index == 0:
            # 요양시설 검색
            url = f'https://openapi.gg.go.kr/OldPersonRecuperationFacility'
            params = {'KEY' : key,'Type' : 'xml', 'pIndex' : 1, 'pSize' : 100, 'SIGUN_NM': search_query}
            response = requests.get(url, params=params)
            
            root = ET.fromstring(response.text)
            
            for item in root.iter('row'):
                name = item.findtext('BIZPLC_NM') #시설명
                capa = item.findtext('ENTRNC_PSN_CAPA') #입소 정원
                qual = item.findtext('QUALFCTN_POSESN_PSN_CNT') #자격증 소유 인원
                area = item.findtext('LOCPLC_AR') #면적
                
                #listbox에 검색 결과 출력, 추후 출력 내용 변경 필요, 정보가 없는게 생각보다 많음
                self.lboxlist[tab_index].insert(END,"시설명 : " + name + "입소 정원 : " + capa + "자격소유인원 : " + qual + "면적 : " + area)


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
            root = ET.fromstring(response.text)
            
            for item in root.iter('row'):
                name = item.findtext('HOSPTL_NM') #병원명
                capa = item.findtext('SICKBD_CNT') #병상 수
                qual = item.findtext('TREAT_SBJECT_CNT') #진료 과목 수
                area = item.findtext('TREAT_SBJECT_DTLS') #진료 과목 내용
                
                #listbox에 검색 결과 출력, 추후 출력 내용 변경 필요
                #위치 정보도 있음, 홈페이지 주소도.
                self.lboxlist[tab_index].insert(END,"병원명 : " + name + "병상 수 : " + capa  + "진료 과목 내용 : (" + qual + "개), " + area)
        
        elif tab_index == 2:
            # 여가복지시설 검색
            url = f'https://openapi.gg.go.kr/SenircentFaclt'
            params = {'KEY' : key,'Type' : 'xml', 'pIndex' : 1, 'pSize' : 100, 'SIGUN_NM': search_query}
            response = requests.get(url)
            
            root = ET.fromstring(response.text)
            
            for item in root.iter('row'):
                name = item.findtext('FACLT_NM') #시설명
                capa = item.findtext('USE_MBER_CNT') #이용중인 회원 수
                num = item.findtext('DETAIL_TELNO') #전화번호
                depart = item.findtext('JURISD_CHARGE_DEPT_NM') #관할 담당 부서
                
                self.lboxlist[tab_index].insert(END,"시설명 : " + name + " 전화번호 : " + num + " 회원 수 : " + capa + " 관할 부서 : " + depart)

        elif tab_index == 3:
            # 의료복지시설 검색
            url = f'https://openapi.gg.go.kr/OldpsnMedcareWelfac'
            params = {'KEY' : key,'Type' : 'xml', 'pIndex' : 1, 'pSize' : 100, 'SIGUN_NM': search_query}
            response = requests.get(url)
            
            root = ET.fromstring(response.text)
            
            for item in root.iter('row'):
                name = item.findtext('FACLT_NM') #시설명
                facl_type = item.findtext('FACLT_KIND_NM') #시설 종류
                qual = item.findtext('LNGTR_RECPER_APPONT_INST_YN_NM') #장기요양지정 여부
                capa = item.findtext('ENTRNC_PSN_CAPA') #입소 정원
                
                self.lboxlist[tab_index].insert(END,"시설 종류 : " + facl_type + " 시설명 : " + name + " 장기요양지정 여부 : " + qual + " 입소 정원 : " + capa)

        elif tab_index == 4:
            # 일자리지원기관 검색
            url = f''
            params ={'KEY' : key,'Type' : 'xml', 'pIndex' : 1, 'pSize' : 100, 'SIGUN_NM': search_query}
            response = requests.get(url)
            
            root = ET.fromstring(response.text)
            
            for item in root.iter('row'):
                name = item.findtext('HOSPTL_NM') #병원명
                capa = item.findtext('SICKBD_CNT') #병상 수
                qual = item.findtext('TREAT_SBJECT_CNT') #진료 과목 수
                area = item.findtext('TREAT_SBJECT_DTLS') #진료 과목 내용
                
                #listbox에 검색 결과 출력, 추후 출력 내용 변경 필요
                #위치 정보도 있음, 홈페이지 주소도.
                self.lboxlist[tab_index].insert(END,"병원명 : " + name + "병상 수 : " + capa  + "진료 과목 내용 : (" + qual + "개), " + area)

        elif tab_index == 5:
            # 주거복지시설 검색
            url = f''
            params = {'KEY' : key,'Type' : 'xml', 'pIndex' : 1, 'pSize' : 100, 'SIGUN_NM': search_query}
            response = requests.get(url)
            
            root = ET.fromstring(response.text)
            
            for item in root.iter('row'):
                name = item.findtext('HOSPTL_NM') #병원명
                capa = item.findtext('SICKBD_CNT') #병상 수
                qual = item.findtext('TREAT_SBJECT_CNT') #진료 과목 수
                area = item.findtext('TREAT_SBJECT_DTLS') #진료 과목 내용
                
                #listbox에 검색 결과 출력, 추후 출력 내용 변경 필요
                #위치 정보도 있음, 홈페이지 주소도.
                self.lboxlist[tab_index].insert(END,"병원명 : " + name + "병상 수 : " + capa  + "진료 과목 내용 : (" + qual + "개), " + area)

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