from tkinter import *
import googlemaps
from PIL import Image, ImageTk
import io
import requests
import tkinter.ttk
import xml.etree.ElementTree as ET
import pickle
from tkinter import messagebox
from keys import *

gmaps = googlemaps.Client(key=google_key)

cvwidth = 425
cvheight = 300
mapcvwidth = 350
mapcvheight = 300

class MainGUI:
    def zoom_in(self, tab_index):
        # 확대 레벨 증가
        self.zoom_level += 1

        # 지도 업데이트
        self.update_map(tab_index)

    def zoom_out(self, tab_index):
        # 확대 레벨 감소
        self.zoom_level -= 1

        # 지도 업데이트
        self.update_map(tab_index)

    def update_map(self, tab_index):
        # 기존 이미지 삭제
        self.mapcanv[tab_index].delete("map_image")

        # 선택된 항목 가져오기
        cur = self.lboxlist[tab_index].curselection()
        if not cur:
            return
        item = self.lboxlist[tab_index].get(cur)

        # 주소 정보 가져오기
        geocode_result = gmaps.geocode(item)
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            lat, lng = location['lat'], location['lng']
            # 지도 URL 업데이트
            map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom={self.zoom_level}&size=400x300&key={google_key}"

            # 마커 추가
            marker_url = f"&markers=color:red%7C{lat},{lng}"
            map_url += marker_url

            # 지도 이미지 다운로드
            img_data = requests.get(map_url).content
            img = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)))

            # 지도 이미지 출력
            self.mapcanv[tab_index].create_image(0, 0, anchor="nw", image=img, tags="map_image")
            self.mapcanv[tab_index].image = img  # 저장하여 참조 유지

    def add_to_bookmarks(self, bookmark):
        # 즐겨찾기에 항목 추가하는 메소드
        self.bookmarks.append(bookmark)
        self.save_bookmarks()  # 변경된 즐겨찾기 정보 저장

    def save_bookmarks(self):
        # 즐겨찾기 정보를 파일로 저장하는 메소드
        with open(self.bookmark_file, "wb") as f:
            pickle.dump(self.bookmarks, f)

    def load_bookmarks(self):
        # 저장된 즐겨찾기 정보를 파일에서 로드하는 메소드
        try:
            with open(self.bookmark_file, "rb") as f:
                self.bookmarks = pickle.load(f)
        except FileNotFoundError:
            # 파일이 존재하지 않는 경우 빈 리스트로 초기화
            self.bookmarks = []

    def add_current_to_bookmarks(self, tab_index):
        # 현재 선택된 정보를 즐겨찾기에 추가하는 메소드
        selected_index = self.lboxlist[tab_index].curselection()
        if selected_index:
            selected_info = self.lboxlist[tab_index].get(selected_index[0])
            self.add_to_bookmarks(selected_info)
            messagebox.showinfo("즐겨찾기 추가", "즐겨찾기에 추가되었습니다.")

            # 즐겨찾기된 정보를 해당 리스트박스에 추가
            self.lboxlist[6].insert(END, selected_info)

    def search(self, tab_index):
        search_query = self.entrylist[tab_index].get()
        self.lboxlist[tab_index].delete(0,END)  # 검색 결과 초기화
        root = NONE
        
        self.ad_list.clear()
        self.canvlist[tab_index].delete('all')
        
        if tab_index == 0:
            # 요양시설 검색
            url = f'https://openapi.gg.go.kr/OldPersonRecuperationFacility'
            params = {'KEY' : key,'Type' : 'xml', 'pIndex' : 1, 'pSize' : 100, 'SIGUN_NM': search_query}
            response = requests.get(url, params=params)
            
            root = ET.fromstring(response.text)
            ad_list = []
            for item in root.iter('row'):
                if item.findtext('BSN_STATE_NM') == '폐업' :
                    continue
                
                name = item.findtext('BIZPLC_NM') #시설명
                address = item.findtext('REFINE_ROADNM_ADDR') #주소
                
                self.ad_list.append(address)
                #listbox에 검색 결과 출력, 추후 출력 내용 변경 필요, 정보가 없는게 생각보다 많음
                self.lboxlist[tab_index].insert(END,"시설명 : " + name + ' 주소 : ' + address)

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
                self.ad_list.append(item.findtext('REFINE_ROADNM_ADDR'))
                
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
            self.canvlist[tab_index].create_text(10 + 0*barWidth + (barWidth / 2),cvheight - 10,text="병상 수")
            self.canvlist[tab_index].create_text(10 + 2*barWidth + (barWidth / 2),cvheight - 10,text="진료과목 수")
            
            self.canvlist[tab_index].create_rectangle(cvwidth - 30, cvheight // 2 + 5 , cvwidth - 15 , cvheight // 2 + 20,tag='config',fill='red')
            self.canvlist[tab_index].create_text(cvwidth - 23,cvheight//2 + 27,text="평균")
            self.canvlist[tab_index].create_rectangle(cvwidth - 30, cvheight // 2 + 55 , cvwidth - 15 , cvheight // 2 + 70,tag='config',fill='blue')
            self.canvlist[tab_index].create_text(cvwidth - 23,cvheight//2 + 77,text="시설")

        elif tab_index == 2:
            # 여가복지시설 검색
            url = f'https://openapi.gg.go.kr/SenircentFaclt'
            params = {'KEY': key, 'Type': 'xml', 'pIndex': 1, 'pSize': 100, 'SIGUN_NM': search_query}
            response = requests.get(url,params=params)
            
            root = ET.fromstring(response.text)
            
            for item in root.iter('row'):
                name = item.findtext('FACLT_NM') #시설명
                num = item.findtext('DETAIL_TELNO') #전화번호
                if num == '' :
                    num = '-'
                self.ad_list.append(item.findtext('REFINE_ROADNM_ADDR'))
                
                self.lboxlist[tab_index].insert(END,"시설명 : " + name + " 전화번호 : " + num)

        elif tab_index == 3:
            # 의료복지시설 검색
            url = f'https://openapi.gg.go.kr/OldpsnMedcareWelfac'
            params = {'KEY' : key,'Type' : 'xml', 'pIndex' : 1, 'pSize' : 100, 'SIGUN_NM': search_query}
            response = requests.get(url,params=params)
            
            root = ET.fromstring(response.text)
            
            self.index3_tuple_list.clear()
            
            avg_capa = 0
            avg_size = 0
            avg_qual = 0
            count = 0
            
            self.max_capa = 0
            self.max_qual = 0
            self.max_size = 0
            
            for item in root.iter('row'):
                name = item.findtext('FACLT_NM') #시설명
                qual = item.findtext('LNGTR_RECPER_APPONT_INST_YN_NM') #장기요양지정 여부
                telnum = item.findtext('DETAIL_TELNO') #전화번호
                if telnum == '' :
                    telnum = '-'
                capa = item.findtext('ENTRNC_PSN_CAPA') #입소 정원
                cur_size = item.findtext('ENTRNC_PSTPSN_SUM') #입소 현원
                cur_qual = item.findtext('ENFLPSN_PSTPSN_SUM') #종사 현원
                
                avg_capa += int(capa)
                if self.max_capa < int(capa) :
                    self.max_capa = int(capa)
                avg_size += int(capa) - int(cur_size)
                if self.max_size < int(capa) - int(cur_size) :
                    self.max_size = int(capa) - int(cur_size)
                avg_qual += int(cur_qual)
                if self.max_qual < int(cur_qual) :
                    self.max_qual = int(cur_qual)
                
                count += 1
                
                self.index3_tuple_list.append((int(capa), int(cur_size), int(cur_qual)))
                self.ad_list.append(item.findtext('REFINE_ROADNM_ADDR'))
                
                self.lboxlist[tab_index].insert(END,"시설명 : " + name + " 장기요양지정 여부 : " + qual + " 전화번호 : " + telnum)
            
            barWidth = (cvwidth - 10) / 6 - 10
            
            self.canvlist[tab_index].create_rectangle(20 + 0*barWidth + 10, cvheight - (avg_capa // count / self.max_capa)*3 * cvheight - 10, 10 + 1*barWidth,cvheight - 20,tags='avg',fill='red')
            self.canvlist[tab_index].create_rectangle(20 + 2*barWidth + 10, cvheight - (avg_size // count / self.max_size)*3 * cvheight - 10, 10 + 3*barWidth,cvheight - 20,tags='avg',fill='red')
            self.canvlist[tab_index].create_rectangle(20 + 4*barWidth + 10, cvheight - (avg_qual // count / self.max_qual)*3 * cvheight - 10, 10 + 5*barWidth,cvheight - 20,tags='avg',fill='red')
            
            self.canvlist[tab_index].create_text(20 + 0*barWidth + (barWidth / 2),cvheight - 10,text="입소 정원")
            self.canvlist[tab_index].create_text(20 + 2*barWidth + (barWidth / 2),cvheight - 10,text="공석")
            self.canvlist[tab_index].create_text(20 + 4*barWidth + (barWidth / 2),cvheight - 10,text="종사원수")
            
            self.canvlist[tab_index].create_rectangle(cvwidth - 30, cvheight // 2 + 5 , cvwidth - 15 , cvheight // 2 + 20,tag='config',fill='red')
            self.canvlist[tab_index].create_text(cvwidth - 23,cvheight//2 + 27,text="평균")
            self.canvlist[tab_index].create_rectangle(cvwidth - 30, cvheight // 2 + 55 , cvwidth - 15 , cvheight // 2 + 70,tag='config',fill='blue')
            self.canvlist[tab_index].create_text(cvwidth - 23,cvheight//2 + 77,text="시설")

        elif tab_index == 4:
            # 일자리지원기관 검색
            url = f'https://openapi.gg.go.kr/OldpsnJobSportInst'
            params ={'KEY' : key,'Type' : 'xml', 'pIndex' : 1, 'pSize' : 100, 'SIGUN_NM': search_query}
            response = requests.get(url,params=params)
            
            root = ET.fromstring(response.text)
            
            self.index4_tuple_list.clear()
            
            self.max_qual = 0
            self.max_area = 0
            
            avg_qual = 0
            avg_area = 0
            count = 0
            
            for item in root.iter('row'):
                name = item.findtext('FACLT_NM') #시설명
                qual = item.findtext('ENFLPSN_PSTPSN_SUM') #종사자현원
                telno = item.findtext('DETAIL_TELNO') #전화번호
                area = item.findtext('FACLT_AR_SUM')
                self.ad_list.append(item.findtext('REFINE_ROADNM_ADDR'))
                
                avg_qual += int(qual)
                avg_area += int(area)
                count += 1
                
                if self.max_area < int(area) :
                    self.max_area = int(area)
                if self.max_qual < int(qual) :
                    self.max_qual = int(qual)
                
                self.index4_tuple_list.append((int(area), int(qual)))
                
                self.lboxlist[tab_index].insert(END,"시설명 : " + name + " 종사자 현원 : " + qual + " 전화번호 : " + telno)
            barWidth = (cvwidth - 10) / 4 - 10
            
            self.canvlist[tab_index].create_rectangle(10 + 0*barWidth + 5, cvheight - (avg_qual // count / self.max_qual) * cvheight - 10, 10 + 1*barWidth,cvheight - 20,tags='avg',fill='red')
            self.canvlist[tab_index].create_rectangle(10 + 2*barWidth + 5, cvheight - (avg_area // count / self.max_area)*10 * cvheight - 10, 10 + 3*barWidth,cvheight - 20,tags='avg',fill='red')
            
            self.canvlist[tab_index].create_text(10 + 0*barWidth + (barWidth / 2),cvheight - 10,text="종사 현원")
            self.canvlist[tab_index].create_text(10 + 2*barWidth + (barWidth / 2),cvheight - 10,text="총 면적")
            
            self.canvlist[tab_index].create_rectangle(cvwidth - 30, cvheight // 2 + 5 , cvwidth - 15 , cvheight // 2 + 20,tag='config',fill='red')
            self.canvlist[tab_index].create_text(cvwidth - 23,cvheight//2 + 27,text="평균")
            self.canvlist[tab_index].create_rectangle(cvwidth - 30, cvheight // 2 + 55 , cvwidth - 15 , cvheight // 2 + 70,tag='config',fill='blue')
            self.canvlist[tab_index].create_text(cvwidth - 23,cvheight//2 + 77,text="시설")

        elif tab_index == 5:
            # 주거복지시설 검색
            url = f'https://openapi.gg.go.kr/OldpsnHousngWelfaclt'
            params = {'KEY' : key,'Type' : 'xml', 'pIndex' : 1, 'pSize' : 100, 'SIGUN_NM': search_query}
            response = requests.get(url,params=params)
            
            root = ET.fromstring(response.text)
            
            self.index5_tuple_list.clear()
            
            self.max_capa = 0
            self.max_size = 0
            self.max_qual = 0
            
            avg_capa = 0
            avg_size = 0
            avg_qual = 0
            count = 0
            
            for item in root.iter('row'):
                name = item.findtext('FACLT_NM') #시설명
                lot_type = item.findtext('LOTOUT_TYPE') #분양유형
                telno = item.findtext('DETAIL_TELNO') #전화번호
                capa = item.findtext('EXPA_HSHLD_CNT_SUM') #총 세대수
                cur_size = item.findtext('ENTRNC_PSTPSN_SUM') #현재 입주 인수
                cur_qual = item.findtext('ENFLPSN_PSTPSN_SUM') #종사자 현원
                self.ad_list.append(item.findtext('REFINE_ROADNM_ADDR'))
                self.index5_tuple_list.append((int(capa), int(cur_size), int(cur_qual)))
                
                avg_capa += int(capa)
                avg_size += int(cur_size)
                avg_qual += int(cur_qual)
                count += 1
                
                if self.max_capa < int(capa) :
                    self.max_capa = int(capa)
                if self.max_size < int(cur_size) :
                    self.max_size = int(cur_size)
                if self.max_qual < int(cur_qual) :
                    self.max_qual = int(cur_qual)
                
                self.lboxlist[tab_index].insert(END,"시설명(유형) : " + name + "(" + lot_type + ")" + " 전화번호 : " + telno)
            
            barWidth = (cvwidth - 10) / 6 - 10
            
            self.canvlist[tab_index].create_rectangle(20 + 0*barWidth + 10, cvheight - (avg_capa // count / self.max_capa) * cvheight - 10, 10 + 1*barWidth,cvheight - 20,tags='avg',fill='red')
            self.canvlist[tab_index].create_rectangle(20 + 2*barWidth + 10, cvheight - (avg_size // count / self.max_size) * cvheight - 10, 10 + 3*barWidth,cvheight - 20,tags='avg',fill='red')
            self.canvlist[tab_index].create_rectangle(20 + 4*barWidth + 10, cvheight - (avg_qual // count / self.max_qual) * cvheight - 10, 10 + 5*barWidth,cvheight - 20,tags='avg',fill='red')
            
            self.canvlist[tab_index].create_text(20 + 0*barWidth + (barWidth / 2),cvheight - 10,text="총 세대수")
            self.canvlist[tab_index].create_text(20 + 2*barWidth + (barWidth / 2),cvheight - 10,text="입소 현원")
            self.canvlist[tab_index].create_text(20 + 4*barWidth + (barWidth / 2),cvheight - 10,text="종사 현원")
            
            self.canvlist[tab_index].create_rectangle(cvwidth - 30, cvheight // 2 + 5 , cvwidth - 15 , cvheight // 2 + 20,tag='config',fill='red')
            self.canvlist[tab_index].create_text(cvwidth - 23,cvheight//2 + 27,text="평균")
            self.canvlist[tab_index].create_rectangle(cvwidth - 30, cvheight // 2 + 55 , cvwidth - 15 , cvheight // 2 + 70,tag='config',fill='blue')
            self.canvlist[tab_index].create_text(cvwidth - 23,cvheight//2 + 77,text="시설")

    def on_select(self,tab_index) : #리스트 박스에서 항목 선택시 실행될 함수
        cur = self.lboxlist[tab_index].curselection()
        
        if not cur :
            return
        
        item = self.lboxlist[tab_index].get(cur)

        if tab_index == 0:
            pass

        elif tab_index == 1:
            self.canvlist[tab_index].delete('data')
            capa = int(item.split("병상 수 : ")[1].split(" ")[0])
            qual = int(item.split("진료 과목 내용 : (")[1].split("개)")[0])
            
            barWidth = (cvwidth - 10) / 4 - 10
            
            self.canvlist[tab_index].create_rectangle(10 + 1*barWidth + 5, cvheight - (capa / self.max_capa) * cvheight - 10, 10 + 2*barWidth,cvheight - 20,tags='data',fill='blue')
            self.canvlist[tab_index].create_rectangle(10 + 3*barWidth + 5, cvheight - (qual / self.max_qual) * cvheight - 10, 10 + 4*barWidth,cvheight - 20,tags='data',fill='blue')
            self.canvlist[tab_index].create_text(10 + 1*barWidth + (barWidth / 2),cvheight - 10,text="병상 수",tags='data')
            self.canvlist[tab_index].create_text(12 + 3*barWidth + (barWidth / 2),cvheight - 10,text="진료과목 수",tags='data')

        elif tab_index == 2:
            pass

        elif tab_index == 3:
            self.canvlist[tab_index].delete('data')
            data = self.index3_tuple_list[cur[0]]
            barWidth = (cvwidth - 10) / 6 - 10
            
            self.canvlist[tab_index].create_rectangle(20 + 1*barWidth + 10, cvheight - (data[0] / self.max_capa)*3 * cvheight - 10, 10 + 2*barWidth,cvheight - 20,tags='data',fill='blue')
            if (data[0] - data[1]) > 0 :
                self.canvlist[tab_index].create_rectangle(20 + 3*barWidth + 10, cvheight - ((data[0] - data[1]) / self.max_size)*3 * cvheight - 10, 10 + 4*barWidth,cvheight - 20,tags='data',fill='blue')
            self.canvlist[tab_index].create_rectangle(20 + 5*barWidth + 10, cvheight - (data[2] / self.max_qual)*3 * cvheight - 10, 10 + 6*barWidth,cvheight - 20,tags='data',fill='blue')
            
            self.canvlist[tab_index].create_text(20 + 1*barWidth + (barWidth / 2),cvheight - 10,text="입소 정원",tags='data')
            self.canvlist[tab_index].create_text(20 + 3*barWidth + (barWidth / 2),cvheight - 10,text="공석",tags='data')
            self.canvlist[tab_index].create_text(20 + 5*barWidth + (barWidth / 2),cvheight - 10,text="종사 현원",tags='data')

        elif tab_index == 4:
            self.canvlist[tab_index].delete('data')
            data = self.index4_tuple_list[cur[0]]
            barWidth = (cvwidth - 10) / 4 - 10
            
            self.canvlist[tab_index].create_rectangle(10 + 1*barWidth + 5, cvheight - (data[1] / self.max_qual) * cvheight - 10, 10 + 2*barWidth,cvheight - 20,tags='data',fill='blue')
            self.canvlist[tab_index].create_rectangle(10 + 3*barWidth + 5, cvheight - (data[0] / self.max_area) *10 * cvheight - 10, 10 + 4*barWidth,cvheight - 20,tags='data',fill='blue')
            
            self.canvlist[tab_index].create_text(10 + 1*barWidth + (barWidth / 2),cvheight - 10,text="종사 현원",tags='data')
            self.canvlist[tab_index].create_text(10 + 3*barWidth + (barWidth / 2),cvheight - 10,text="총 면적",tags='data')

        elif tab_index == 5:
            self.canvlist[tab_index].delete('data')
            data = self.index5_tuple_list[cur[0]]
            barWidth = (cvwidth - 10) / 6 - 10
            
            self.canvlist[tab_index].create_rectangle(20 + 1*barWidth + 10, cvheight - (data[0] / self.max_capa) * cvheight - 10, 10 + 2*barWidth,cvheight - 20,tags='data',fill='blue')
            if data[1] > 0 :
                self.canvlist[tab_index].create_rectangle(20 + 3*barWidth + 10, cvheight - (data[1] / self.max_size) * cvheight - 10, 10 + 4*barWidth,cvheight - 20,tags='data',fill='blue')
            if data[2] > 0 :
                self.canvlist[tab_index].create_rectangle(20 + 5*barWidth + 10, cvheight - (data[2] / self.max_qual) * cvheight - 10, 10 + 6*barWidth,cvheight - 20,tags='data',fill='blue')
            
            self.canvlist[tab_index].create_text(20 + 1*barWidth + (barWidth / 2),cvheight - 10,text="총 세대수",tags='data')
            self.canvlist[tab_index].create_text(20 + 3*barWidth + (barWidth / 2),cvheight - 10,text="입소 현원",tags='data')
            self.canvlist[tab_index].create_text(20 + 5*barWidth + (barWidth / 2),cvheight - 10,text="종사 현원",tags='data')
        
        #선택된 시설의 구글맵 출력
        geocode_result = gmaps.geocode(self.ad_list[cur[0]])
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            lat, lng = location['lat'], location['lng']
            map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=14&size=400x300&key={google_key}"
            # 마커 추가
            marker_url = f"&markers=color:red%7C{lat},{lng}"
            map_url += marker_url

            # 구글 지도 표시
            img_data = requests.get(map_url).content
            img = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)))

            # 선택된 항목에 해당하는 이미지 출력
            self.mapcanv[tab_index].create_image(0, 0, anchor="nw", image=img)
            self.mapcanv[tab_index].image = img  # 저장하여 참조 유지

            # 초기값 설정
            self.center_lat = lat
            self.center_lng = lng
            self.zoom_level = 14

    def __init__(self):
        window = Tk()
        window.title("노인통합 서비스")
        window.geometry("800x600")
        # 즐겨찾기 정보를 저장할 파일 경로
        self.bookmark_file = "bookmark_data.pkl"
        self.bookmarks = []  # 즐겨찾기 정보를 담을 리스트

        # 저장된 즐겨찾기 정보 로드
        self.load_bookmarks()

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

        #검색, 즐겨찾기 버튼
        for i in range(7):
            Button(self.framelist[i], text='검색', command=lambda i=i: self.search(i)).place(x=150, y=10)
            Button(self.framelist[i], text='즐겨찾기', command=lambda i=i: self.add_current_to_bookmarks(i)).place(x=190, y=10)
            Button(self.framelist[i], text='+', command=lambda: self.zoom_in(i)).place(x=435, y=250 + mapcvheight)
            Button(self.framelist[i], text='-', command=lambda: self.zoom_out(i)).place(x=470, y=250 + mapcvheight)

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

        self.ad_list = []
        self.index3_tuple_list = [] #tab_index 3 의료복지센터의 그래프에 필요한 정보를 (입소 정원 , 입소 현원, 종사 현원) 으로 저장하는 리스트
        self.index4_tuple_list = [] #tab_index 4 일자리지원센터의 그래프에 필요한 정보를 (총면적, 종사 현원)으로 저장하는 리스트
        self.index5_tuple_list = [] #tab_index 5 노인주거복지시설의 그래프에 필요한 정보를 (세대수, 입소 현원, 종사자 현원) 으로 저장하는 리스트

        #선택 부분
        for i in range(7):
            self.lboxlist[i].bind("<<ListboxSelect>>", lambda event, i=i: self.on_select(i))

        window.mainloop()


MainGUI()