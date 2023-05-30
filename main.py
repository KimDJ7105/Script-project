from tkinter import *
#import tkinter as tk
import googlemaps
from PIL import Image, ImageTk
import io
import requests
import tkinter.ttk
import xml.etree.ElementTree as ET

key = 'fc79933d2b8f4ef3bdb6190a73ae8314'
#구글지도 키
google_key ='AIzaSyB1AGcPSS2la62Bc5hfYe2udrZbq-HQBlQ'
gmaps = googlemaps.Client(key=google_key)

cvwidth = 425
cvheight = 300
mapcvwidth = 350
mapcvheight = 300

class MainGUI:
    def idx0_Map(self):
        # 정보 요청 주소 및 요청인자 설정
        url = "https://openapi.gg.go.kr/OldPersonRecuperationFacility"
        params = {
            "Key": key,
            "Type": "xml",
            "pIndex": 1,
            "pSize": 100,
        }

        # 위치 정보 가져오기
        response = requests.get(url, params=params)
        root = ET.fromstring(response.content)
        items = root.findall(".//row")

        hospitals = []
        for item in items:
            hospital = {
                "name": item.findtext("BIZPLC_NM"),  # 시설 이름
                "address": item.findtext("REFINE_ROADNM_ADDR"),  # 시설 주소
            }
            hospitals.append(hospital)

        self.img_list0 = [] #이미지 객체를 저장할 리스트

        # 주소를 기반으로 지도 생성 및 저장
        for i, hospital in enumerate(hospitals):
            address = hospital['address']
            geocode_result = gmaps.geocode(address)
            if geocode_result:
                location = geocode_result[0]['geometry']['location']
                lat, lng = location['lat'], location['lng']
                map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=14&size=400x300&key={google_key}"

                # 구글 지도 표시
                img_data = requests.get(map_url).content
                img = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)))
                self.img_list0.append(img) #이미지 객체를 리스트에 저장

    def idx1_Map(self):
        # 정보 요청 주소 및 요청인자 설정
        url = "https://openapi.gg.go.kr/OldPersonSpecialityHospital"
        params = {
            "Key": key,
            "Type": "xml",
            "pIndex": 1,
            "pSize": 100,
        }

        # 위치 정보 가져오기
        response = requests.get(url, params=params)
        root = ET.fromstring(response.content)
        items = root.findall(".//row")

        hospitals = []
        for item in items:
            hospital = {
                "name": item.findtext("HOSP_NM"),  # 병원 이름
                "address": item.findtext("REFINE_ROADNM_ADDR"),  # 병원 주소
            }
            hospitals.append(hospital)

        self.img_list1 = [] #이미지 객체를 저장할 리스트

        # 주소를 기반으로 지도 생성 및 저장
        for i, hospital in enumerate(hospitals):
            address = hospital['address']
            geocode_result = gmaps.geocode(address)
            if geocode_result:
                location = geocode_result[0]['geometry']['location']
                lat, lng = location['lat'], location['lng']
                map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=14&size=400x300&key={google_key}"

                # 구글 지도 표시
                img_data = requests.get(map_url).content
                img = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)))
                self.img_list1.append(img) #이미지 객체를 리스트에 저장

    def idx2_Map(self):
        # 정보 요청 주소 및 요청인자 설정
        url = "https://openapi.gg.go.kr/SenircentFaclt"
        params = {
            "Key": key,
            "Type": "xml",
            "pIndex": 1,
            "pSize": 100,
        }

        # 위치 정보 가져오기
        response = requests.get(url, params=params)
        root = ET.fromstring(response.content)
        items = root.findall(".//row")

        hospitals = []
        for item in items:
            hospital = {
                "name": item.findtext("FACLT_NM"),  # 시설 이름
                "address": item.findtext("REFINE_ROADNM_ADDR"),  # 시설 주소
            }
            hospitals.append(hospital)

        self.img_list2 = []  # 이미지 객체를 저장할 리스트

        # 주소를 기반으로 지도 생성 및 저장
        for i, hospital in enumerate(hospitals):
            address = hospital['address']
            geocode_result = gmaps.geocode(address)
            if geocode_result:
                location = geocode_result[0]['geometry']['location']
                lat, lng = location['lat'], location['lng']
                map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=14&size=400x300&key={google_key}"

                # 구글 지도 표시
                img_data = requests.get(map_url).content
                img = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)))
                self.img_list2.append(img)  # 이미지 객체를 리스트에 저장

    def idx3_Map(self):
        # 정보 요청 주소 및 요청인자 설정
        url = "https://openapi.gg.go.kr/OldpsnMedcareWelfac"
        params = {
            "Key": key,
            "Type": "xml",
            "pIndex": 1,
            "pSize": 100,
        }

        # 위치 정보 가져오기
        response = requests.get(url, params=params)
        root = ET.fromstring(response.content)
        items = root.findall(".//row")

        hospitals = []
        for item in items:
            hospital = {
                "name": item.findtext("FACLT_NM"),  # 시설 이름
                "address": item.findtext("REFINE_ROADNM_ADDR"),  # 시설 주소
            }
            hospitals.append(hospital)

        self.img_list3 = [] #이미지 객체를 저장할 리스트

        # 주소를 기반으로 지도 생성 및 저장
        for i, hospital in enumerate(hospitals):
            address = hospital['address']
            geocode_result = gmaps.geocode(address)
            if geocode_result:
                location = geocode_result[0]['geometry']['location']
                lat, lng = location['lat'], location['lng']
                map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=14&size=400x300&key={google_key}"

                # 구글 지도 표시
                img_data = requests.get(map_url).content
                img = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)))
                self.img_list3.append(img) #이미지 객체를 리스트에 저장

    def idx4_Map(self):
        # 정보 요청 주소 및 요청인자 설정
        url = "https://openapi.gg.go.kr/OldpsnJobSportInst"
        params = {
            "Key": key,
            "Type": "xml",
            "pIndex": 1,
            "pSize": 100,
        }

        # 위치 정보 가져오기
        response = requests.get(url, params=params)
        root = ET.fromstring(response.content)
        items = root.findall(".//row")

        hospitals = []
        for item in items:
            hospital = {
                "name": item.findtext("FACLT_NM"),  # 시설 이름
                "address": item.findtext("REFINE_ROADNM_ADDR"),  # 시설 주소
            }
            hospitals.append(hospital)

        self.img_list4 = [] #이미지 객체를 저장할 리스트

        # 주소를 기반으로 지도 생성 및 저장
        for i, hospital in enumerate(hospitals):
            address = hospital['address']
            geocode_result = gmaps.geocode(address)
            if geocode_result:
                location = geocode_result[0]['geometry']['location']
                lat, lng = location['lat'], location['lng']
                map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=14&size=400x300&key={google_key}"

                # 구글 지도 표시
                img_data = requests.get(map_url).content
                img = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)))
                self.img_list4.append(img) #이미지 객체를 리스트에 저장

    def idx5_Map(self):
        # 정보 요청 주소 및 요청인자 설정
        url = "https://openapi.gg.go.kr/OldpsnHousngWelfaclt"
        params = {
            "Key": key,
            "Type": "xml",
            "pIndex": 1,
            "pSize": 100,
        }

        # 위치 정보 가져오기
        response = requests.get(url, params=params)
        root = ET.fromstring(response.content)
        items = root.findall(".//row")

        hospitals = []
        for item in items:
            hospital = {
                "name": item.findtext("FACLT_NM"),  # 시설 이름
                "address": item.findtext("REFINE_ROADNM_ADDR"),  # 시설 주소
            }
            hospitals.append(hospital)

        self.img_list5 = []  # 이미지 객체를 저장할 리스트

        # 주소를 기반으로 지도 생성 및 저장
        for i, hospital in enumerate(hospitals):
            address = hospital['address']
            geocode_result = gmaps.geocode(address)
            if geocode_result:
                location = geocode_result[0]['geometry']['location']
                lat, lng = location['lat'], location['lng']
                map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=14&size=400x300&key={google_key}"

                # 구글 지도 표시
                img_data = requests.get(map_url).content
                img = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)))
                self.img_list5.append(img)  # 이미지 객체를 리스트에 저장

    def search(self, tab_index):
        search_query = self.entrylist[tab_index].get()
        self.lboxlist[tab_index].delete(0,END)  # 검색 결과 초기화
        root = NONE
        
        self.canvlist[tab_index].delete('all')
        
        if tab_index == 0:
            # 요양시설 검색
            url = f'https://openapi.gg.go.kr/OldPersonRecuperationFacility'
            params = {'KEY' : key,'Type' : 'xml', 'pIndex' : 1, 'pSize' : 100, 'SIGUN_NM': search_query}
            response = requests.get(url, params=params)
            
            root = ET.fromstring(response.text)
            
            for item in root.iter('row'):
                name = item.findtext('BIZPLC_NM') #시설명
                lat = item.findtext('REFINE_WGS84_LAT') #위도
                logt = item.findtext('REFINE_WGS84_LOGT') #경도
                
                #listbox에 검색 결과 출력, 추후 출력 내용 변경 필요, 정보가 없는게 생각보다 많음
                self.lboxlist[tab_index].insert(END,"시설명 : " + name + ' 위도 : ' + lat + ' 경도 : ' + logt)

        elif tab_index == 1:
            # 전문병원 검색
            url = f'https://openapi.gg.go.kr/OldPersonSpecialityHospital'
            params = {'KEY': key, 'Type': 'xml', 'pIndex': 1, 'pSize': 100, 'SIGUN_NM': search_query}
            response = requests.get(url, params=params)
            
            root = ET.fromstring(response.text)
            
            avg_capa = 0
            avg_qual = 0
            count = 0
            self.max_capa = 0
            self.max_qual = 0
            
            for item in root.iter('row'):
                name = item.findtext('HOSPTL_NM') #병원명
                capa = item.findtext('SICKBD_CNT') #병상 수
                qual = item.findtext('TREAT_SBJECT_CNT') #진료 과목 수
                area = item.findtext('TREAT_SBJECT_DTLS') #진료 과목 내용
                
                avg_capa += int(capa)
                avg_qual += int(qual)
                count += 1
                
                if int(capa) > self.max_capa :
                    self.max_capa = int(capa)
                
                if int(qual) > self.max_qual :
                    self.max_qual = int(qual)
                
                #listbox에 검색 결과 출력, 추후 출력 내용 변경 필요
                #위치 정보도 있음, 홈페이지 주소도.
                self.lboxlist[tab_index].insert(END,"병원명 : " + name + " 병상 수 : " + capa  + " 진료 과목 내용 : (" + qual + "개), " + area)
            
            barWidth = (cvwidth - 10) / 4 - 10
            
            self.canvlist[tab_index].create_rectangle(10 + 0*barWidth + 5, cvheight - (avg_capa // count / self.max_capa) * cvheight - 10, 10 + 1*barWidth,cvheight - 20,tags='avg',fill='red')
            self.canvlist[tab_index].create_rectangle(10 + 2*barWidth + 5, cvheight - (avg_qual // count / self.max_qual) * cvheight - 10, 10 + 3*barWidth,cvheight - 20,tags='avg',fill='red')
            self.canvlist[tab_index].create_text(10 + 0*barWidth + (barWidth / 2),cvheight - 10,text="평균 병상 수")
            self.canvlist[tab_index].create_text(10 + 2*barWidth + (barWidth / 2),cvheight - 10,text="평균 진료과목 수")

        elif tab_index == 2:
            # 여가복지시설 검색
            url = f'https://openapi.gg.go.kr/SenircentFaclt'
            params = {'KEY': key, 'Type': 'xml', 'pIndex': 1, 'pSize': 100, 'SIGUN_NM': search_query}
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
        
        if not cur :
            return
        
        item = self.lboxlist[tab_index].get(cur)

        if tab_index == 0:
            # 선택된 항목에 해당하는 이미지 출력
            img = self.img_list0[cur[0]]
            self.mapcanv[0].create_image(0, 0, anchor="nw", image=img)
            self.mapcanv[0].image = img  # 저장하여 참조 유지

        elif tab_index == 1:
            self.canvlist[tab_index].delete('data')
            capa = int(item.split("병상 수 : ")[1].split(" ")[0])
            qual = int(item.split("진료 과목 내용 : (")[1].split("개)")[0])
            
            barWidth = (cvwidth - 10) / 4 - 10
            
            self.canvlist[tab_index].create_rectangle(10 + 1*barWidth + 5, cvheight - (capa / self.max_capa) * cvheight - 10, 10 + 2*barWidth,cvheight - 20,tags='data',fill='blue')
            self.canvlist[tab_index].create_rectangle(10 + 3*barWidth + 5, cvheight - (qual / self.max_qual) * cvheight - 10, 10 + 4*barWidth,cvheight - 20,tags='data',fill='blue')
            self.canvlist[tab_index].create_text(10 + 1*barWidth + (barWidth / 2),cvheight - 10,text="병상 수",tags='data')
            self.canvlist[tab_index].create_text(12 + 3*barWidth + (barWidth / 2),cvheight - 10,text="진료과목 수",tags='data')
            
            # 선택된 항목에 해당하는 이미지 출력
            img = self.img_list1[cur[0]]
            self.mapcanv[1].create_image(0, 0, anchor="nw", image=img)
            self.mapcanv[1].image = img  # 저장하여 참조 유지

        elif tab_index == 2:
            # 선택된 항목에 해당하는 이미지 출력
            img = self.img_list2[cur[0]]
            self.mapcanv[2].create_image(0, 0, anchor="nw", image=img)
            self.mapcanv[2].image = img  # 저장하여 참조 유지

        elif tab_index == 3:
            # 선택된 항목에 해당하는 이미지 출력
            img = self.img_list3[cur[0]]
            self.mapcanv[3].create_image(0, 0, anchor="nw", image=img)
            self.mapcanv[3].image = img  # 저장하여 참조 유지

        elif tab_index == 4:
            # 선택된 항목에 해당하는 이미지 출력
            img = self.img_list4[cur[0]]
            self.mapcanv[4].create_image(0, 0, anchor="nw", image=img)
            self.mapcanv[4].image = img  # 저장하여 참조 유지

        elif tab_index == 5:
            # 선택된 항목에 해당하는 이미지 출력
            img = self.img_list5[cur[0]]
            self.mapcanv[5].create_image(0, 0, anchor="nw", image=img)
            self.mapcanv[5].image = img  # 저장하여 참조 유지

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
        
        self.entrylist = [] #엔트리가 담길 리스트
        self.lboxlist = [] #리스트 박스가 담길 리스트
        self.canvlist = [] #켄버스가 담길 리스트
        self.mapcanv = [] #구글지도 캔버스

        for i in range(7):
            self.entrylist.append(Entry(self.framelist[i], width=19))
            self.entrylist[i].place(x=10, y=10)

            self.lboxlist.append(Listbox(self.framelist[i], width=60, height=10))
            self.lboxlist[i].place(x=5, y=80)
            # 리스트박스 스크롤바
            scrollbar = Scrollbar(self.framelist[i])
            self.lboxlist[i].config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=self.lboxlist[i].yview)
            scrollbar.place(x=420, y=70, height=180)

            self.canvlist.append(Canvas(self.framelist[i], bg='white', width=cvwidth, height=cvheight))
            self.canvlist[i].place(x=5, y=250)

            self.mapcanv.append(Canvas(self.framelist[i], bg='white', width=mapcvwidth, height=mapcvheight))
            self.mapcanv[i].place(x=435, y=250)

            #구글 지도
        self.idx0_Map()
        self.idx1_Map()
        #self.idx2_Map() 공공api 주소 문제?, 일시적인 오류?
        self.idx3_Map()
        self.idx4_Map()
        #self.idx5_Map() 공공api 주소 문제?, 일시적인 오류?

        self.lboxlist[0].bind("<<ListboxSelect>>", lambda event : self.on_select(0))
        self.lboxlist[1].bind("<<ListboxSelect>>", lambda event : self.on_select(1))
        self.lboxlist[2].bind("<<ListboxSelect>>", lambda event : self.on_select(2))
        self.lboxlist[3].bind("<<ListboxSelect>>", lambda event : self.on_select(3))
        self.lboxlist[4].bind("<<ListboxSelect>>", lambda event : self.on_select(4))
        self.lboxlist[5].bind("<<ListboxSelect>>", lambda event : self.on_select(5))
        self.lboxlist[6].bind("<<ListboxSelect>>", lambda event : self.on_select(6))
        window.mainloop()


MainGUI()