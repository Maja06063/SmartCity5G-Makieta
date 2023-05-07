#!/usr/bin/python3

from requests import get, post
from hashlib import md5
from time import sleep

def print_direction(direction: int) -> str:

    if direction == 1:
        return "W lewo"

    elif direction == 2:
        return "W prawo"

    elif direction == 3:
        return "Prosto"

    elif direction == 4:
        return "Cel osiągnięty"

    else:
        return "Bład"

def test_get(token: int, distanece: int):

    parameters = {"distance_cm": distanece, "token": token}
    response = get("http://127.0.0.1:5000/direction", json = parameters)

    if response.status_code == 200:
        print(response.json())
        print(print_direction(response.json()["turn_direction"]))

login = "user123"
passwd = "jakiesHaslo"

# Haszowanie hasła

passoword_bytes = passwd.encode() # encode zwraca bajty ze stringa password
md5_bites = md5(passoword_bytes).digest() # md5 wylicza md5 (hasz) z podanych bajtow, a digest zamienia obiekt md5 na bajty
passwd_hash = int.from_bytes(md5_bites, 'big') # zamiana bajtow na inta, big oznacza ze najbardziej znaczacy bajt jest na początku
# metoda from_bytes która konwertuje bajty na inty
print("Haszowane haslo: ", passwd_hash)

# Odkomentuj właściwy test:

# 1. Test POSTa z danymi logowania:
parameters = {"user": login, "pass": passwd_hash}
response = post("http://127.0.0.1:5000/auth", json = parameters)

if response.status_code == 200:
    print(response.json())
    token = response.json()["token"]
    print(token)

sleep(3)

# 2. Test GETa z odległością przed skrętem:
test_get(token, 60)
sleep(3)

# 3. Test GETa z odległością zmuszającą do skrętu:
test_get(token, 9)
sleep(3)

# 4. Test GETa z odległością informującą o pokonaniu skrętu:
test_get(token, 35)
sleep(3)

# 4. Test GETa z odległością informującą o konieczności skrętu:
test_get(token, 9)
sleep(3)

# 5. Test GETa z odległością informującą o zaparkowaniu:
test_get(token, 2)
