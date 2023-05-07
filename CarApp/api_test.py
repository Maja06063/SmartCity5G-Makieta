from requests import get, post
from hashlib import md5

firstInt = 1
seconInt = '2'

# Haszowanie hasła

passoword_bytes = seconInt.encode() # encode zwraca bajty ze stringa password
md5_bites = md5(passoword_bytes).digest() # md5 wylicza md5 (hasz) z podanych bajtow, a digest zamienia obiekt md5 na bajty
seconInt = int.from_bytes(md5_bites, 'big') # zamiana bajtow na inta, big oznacza ze najbardziej znaczacy bajt jest na początku
# metoda from_bytes która konwertuje bajty na inty
# print("Haszowane haslo: ", seconInt)

# Odkomentuj właściwy test:

# 1. Test POSTa z danymi logowania:
parameters = {"user": firstInt, "pass": seconInt}
response = post("http://127.0.0.1:5000/auth", json = parameters)
###

# 2. Test GETa z odległością:
#parameters = {"distance_cm": firstInt, "token": seconInt}
#response = get("http://127.0.0.1:5000/direction", json = parameters)
###

if response.status_code == 200:
    print(response.json())