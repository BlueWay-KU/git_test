import requests
import json

def FromWeb(ID):
    data = {"ID":ID} 
    r = requests.get("http://dbwo4011.cafe24.com/KO/KOREA/loadData.php",params = data)

    r.encoding = 'UTF-8'
    Data = json.loads(r.text)

    length = len(Data)

    return Data[length-1]['DATA']
