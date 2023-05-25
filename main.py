from tkinter import *
import folium
import webbrowser
import requests
import tkinter.ttk
import xml.etree.ElementTree as ET

key = 'fc79933d2b8f4ef3bdb6190a73ae8314'

class MainGUI:
    #folium 지도
    def MapUI(self, tab_index):
        map_osm = folium.Map(location=[37.3402849,126.7313189], zoom_start =13)
        folium.Marker([37.3402849,126.7313189],popup='위치').add_to(map_osm)
        map_osm.save('osm.html')
        webbrowser.open_new('osm.html')

    def search(self, tab_index):
        search_query = self.entrylist[tab_index].get()
        self.search_results = []  # 검색 결과 초기화
        root = NONE
        
        
        
        print()
        #self.lboxlist[tab_index].delete(0,END)
    
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
            response = requests.get(url,params=params)
            
            
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
            response = requests.get(url,params=params)
            
            root = ET.fromstring(response.text)
            
            for item in root.iter('row'):
                name = item.findtext('FACLT_NM') #시설명
                facl_type = item.findtext('FACLT_KIND_NM') #시설 종류
                qual = item.findtext('LNGTR_RECPER_APPONT_INST_YN_NM') #장기요양지정 여부
                capa = item.findtext('ENTRNC_PSN_CAPA') #입소 정원
                
                self.lboxlist[tab_index].insert(END,"시설 종류 : " + facl_type + " 시설명 : " + name + " 장기요양지정 여부 : " + qual + " 입소 정원 : " + capa)

        elif tab_index == 4:
            # 일자리지원기관 검색
            url = f'https://openapi.gg.go.kr/OldpsnJobSportInst'
            params ={'KEY' : key,'Type' : 'xml', 'pIndex' : 1, 'pSize' : 100, 'SIGUN_NM': search_query}
            response = requests.get(url,params=params)
            
            root = ET.fromstring(response.text)
            
            for item in root.iter('row'):
                name = item.findtext('FACLT_NM') #시설명
                qual = item.findtext('ENFLPSN_PSN_CAPA') #종사자정원
                instl = item.findtext('PRVATE_INSTL_DIV_NM') #설치 주체
                op = item.findtext('INSTL_MAINBD_DIV_NM') #운영 주체
                
                self.lboxlist[tab_index].insert(END,"시설명 : " + name + " 종사자 정원 : " + qual + " 설치/운영 : " + instl + " / " + op)

        elif tab_index == 5:
            # 주거복지시설 검색
            url = f'https://openapi.gg.go.kr/OldpsnHousngWelfaclt'
            params = {'KEY' : key,'Type' : 'xml', 'pIndex' : 1, 'pSize' : 100, 'SIGUN_NM': search_query}
            response = requests.get(url,params=params)
            
            root = ET.fromstring(response.text)
            
            for item in root.iter('row'):
                name = item.findtext('FACLT_NM') #시설명
                lot_type = item.findtext('LOTOUT_TYPE') #분양유형
                qual = item.findtext('EXPA_HSHLD_CNT_SUM') #총 세대수
                c_capa = item.findtext('ENTRNC_PSTPSN_SUM') #입소현원
                
                self.lboxlist[tab_index].insert(END,"시설명(유형) : " + name + "(" + lot_type + ")" + " 총 세대수 / 입소현원 : " + qual + " / " + c_capa)

    def on_select(self,tab_index) : #리스트 박스에서 항목 선택시 실행될 함수
        cur = self.lboxlist[tab_index].curselection()
        
        if cur :
            item = self.lboxlist[tab_index].get(cur)
            print(item)

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
        #folium 지도 전분병원 검색 하는중
        Button(self.framelist[1], text='지도', command=lambda: self.MapUI(1)).place(x=190, y=10)

        Button(self.framelist[2], text='검색', command=lambda: self.search(2)).place(x=150, y=10)
        Button(self.framelist[3], text='검색', command=lambda: self.search(3)).place(x=150, y=10)
        Button(self.framelist[4], text='검색', command=lambda: self.search(4)).place(x=150, y=10)
        Button(self.framelist[5], text='검색', command=lambda: self.search(5)).place(x=150, y=10)
        Button(self.framelist[6], text='검색', command=lambda: self.search(6)).place(x=150, y=10)
        
        self.entrylist = [] #엔트리가 담길 리스트
        self.lboxlist = [] #리스트 박스가 담길 리스트
        self.labellist = [] #라벨이 담길 리스트

        for i in range(7):
            self.entrylist.append(Entry(self.framelist[i], width=19))
            self.entrylist[i].place(x=10, y=10)
            
            self.lboxlist.append(Listbox(self.framelist[i],width=60,height=10))
            self.lboxlist[i].place(x=5,y=80)
            
            self.labellist.append(Label(self.framelist[i],bg='white',width=60,height=25))
            self.labellist[i].place(x=5,y=250)
        
        self.lboxlist[0].bind("<<ListboxSelect>>", lambda event : self.on_select(0))
        self.lboxlist[1].bind("<<ListboxSelect>>", lambda event : self.on_select(1))
        self.lboxlist[2].bind("<<ListboxSelect>>", lambda event : self.on_select(2))
        self.lboxlist[3].bind("<<ListboxSelect>>", lambda event : self.on_select(3))
        self.lboxlist[4].bind("<<ListboxSelect>>", lambda event : self.on_select(4))
        self.lboxlist[5].bind("<<ListboxSelect>>", lambda event : self.on_select(5))
        self.lboxlist[6].bind("<<ListboxSelect>>", lambda event : self.on_select(6))
        
        window.mainloop()


MainGUI()