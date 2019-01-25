import requests
import json
import sensor

ID = 2
DATA = sensor.fire()

print DATA

data = {"ID":ID,"DATA":DATA}
r = requests.get("http://dbwo4011.cafe24.com/KO/KOREA/saveData.php",params = data)
print(r.text)
