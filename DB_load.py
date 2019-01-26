import requests
import json

def FromWeb(ID):
    data = {"ID":ID} 
    r = requests.get("http://dbwo4011.cafe24.com/KO/KOREA/loadData.php",params = data)

    r.encoding = 'UTF-8'
    Data = json.loads(r.text)

    length = len(Data)

    return Data[length-1]['DATA']

User = FromWeb(1)
print("User Location: "+User)

Fire = FromWeb(2)
print("Fire Location: "+Fire)

"""
ID_1 = 1 
data_1 = {"ID":ID_1} 
r_1 = requests.get("http://dbwo4011.cafe24.com/KO/KOREA/loadData.php",params = data_1)
r_1.encoding = 'UTF-8'
Data_1 = json.loads(r_1.text)

#print(Data_1)
length_1 = len(Data_1)
#print(length_1)

print("User Location: "+Data_1[length_1-1]['DATA']) 

ID_2 = 2
data_2 = {"ID":ID_2} 
r_2 = requests.get("http://dbwo4011.cafe24.com/KO/KOREA/loadData.php",params = data_2)
r_2.encoding = 'UTF-8'
Data_2 = json.loads(r_2.text)

#print(Data_2)
length_2 = len(Data_2)
#print(length_2)

print("Fire Location: "+Data_2[length_2-1]['DATA']) 
"""

"""
import requests
import json

ID = 1
data = {"ID":ID} 
r = requests.get("http://dbwo4011.cafe24.com/KO/KOREA/loadData.php",params = data)
print(r.text)
print(type(r.text))
r.encoding = 'UTF-8'
Data = json.loads(r.text)

print(Data[0]['ID']+" // "+Data[0]['DATA']) 

"""
