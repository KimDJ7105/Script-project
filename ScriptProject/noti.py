#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
import requests
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback
import xml.etree.ElementTree as ET
import keys

key = keys.key
TOKEN = '6009726152:AAGffpVsw-WD5EUwZeqEfD_H9YFOAlHui1o'
MAX_MSG_LENGTH = 300
bot = telepot.Bot(TOKEN)

url_list = []

url_list.append('https://openapi.gg.go.kr/OldPersonRecuperationFacility')
url_list.append('https://openapi.gg.go.kr/OldPersonSpecialityHospital')
url_list.append('https://openapi.gg.go.kr/OldpsnMedcareWelfa')
url_list.append('https://openapi.gg.go.kr/OldpsnJobSportInst')
url_list.append('https://openapi.gg.go.kr/OldpsnHousngWelfaclt')

def getData(url_index, loc_param):
    res_list = []
    params = {'KEY' : key,'Type' : 'xml', 'pIndex' : 1, 'pSize' : 100, 'SIGUN_NM': loc_param}
    response = requests.get(url_list[url_index], params=params)
    
    root = ET.fromstring(response.text)
    
    if url_index == 0 :
        for item in root.iter('row'):
            if item.findtext('BSN_STATE_NM') == '폐업' :
                continue
            area = item.findtext('SIGUN_NM') #지역
            name = item.findtext('BIZPLC_NM') #시설명
            address = item.findtext('REFINE_ROADNM_ADDR') #주소

            res_list.append('<' + area + '> ' + name + ' 주소 : ' + address)
    
    if url_index == 1:
        for item in root.iter('row'):
            Harea = item.findtext('SIGUN_NM')  # 지역
            name = item.findtext('HOSPTL_NM') #병원명
            qual = item.findtext('TREAT_SBJECT_DTLS') #진료 과목 내용

            res_list.append('<' + Harea + '> ' + name + ' 진료 과목 : ' + qual)
    
    if url_index == 2:
        for item in root.iter('row'):
            area = item.findtext('SIGUNGU_NM') #지역
            name = item.findtext('FACLT_NM') #시설명
            telnum = item.findtext('DETAIL_TELNO') #전화번호
            
            res_list.append('<' + area + '> ' + name + ' 전화번호 : ' + telnum)
    
    if url_index == 3 :
        for item in root.iter('row'):
            Harea = item.findtext(('SIGUN_NM')) #지역
            name = item.findtext('FACLT_NM') #시설명
            telno = item.findtext('DETAIL_TELNO') #전화번호
            
            res_list.append('<' + Harea + '> ' + name + ' 전화번호 : ' + telno)
    
    if url_index == 4 :
        for item in root.iter('row'):
            area = item.findtext(('SIGUN_NM'))  # 지역
            name = item.findtext('FACLT_NM') #시설명
            lot_type = item.findtext('LOTOUT_TYPE') #분양유형
            telno = item.findtext('DETAIL_TELNO') #전화번호
            
            res_list.append('<' + area + '> ' + name + ' 분양유형 : ' + lot_type + ' 전화번호 : ' + telno)
    
    return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)

def run(date_param, param='11710'):
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs( user TEXT, log TEXT, PRIMARY KEY(user, log) )')
    conn.commit()

    user_cursor = sqlite3.connect('users.db').cursor()
    user_cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    user_cursor.execute('SELECT * from users')

    for data in user_cursor.fetchall():
        user, param = data[0], data[1]
        print(user, date_param, param)
        res_list = getData( param, date_param )
        msg = ''
        for r in res_list:
            try:
                cursor.execute('INSERT INTO logs (user,log) VALUES ("%s", "%s")'%(user,r))
            except sqlite3.IntegrityError:
                # 이미 해당 데이터가 있다는 것을 의미합니다.
                pass
            else:
                print( str(datetime.now()).split('.')[0], r )
                if len(r+msg)+1>MAX_MSG_LENGTH:
                    sendMessage( user, msg )
                    msg = r+'\n'
                else:
                    msg += r+'\n'
        if msg:
            sendMessage( user, msg )
    conn.commit()

if __name__=='__main__':
    today = date.today()
    current_month = today.strftime('%Y%m')

    print( '[',today,']received token :', TOKEN )

    pprint( bot.getMe() )

    run(current_month)
