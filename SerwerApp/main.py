#!/usr/bin/python3

from flask import Flask, request
import json
from state_machine import StateMachine, WhereDrive
import random

remembered_token = 0
TEST_USER = "user123"
TEST_MD5 = 81548367024625717545001236878397010683
states = StateMachine()

"""
Funkcja check_authentication służy do sprawdzenia czy samochód przesłał
poprawny login i hasło i jeśli tak, do wygenerowania i zachowania na potem tokenu.
"""
def check_authentication(user: str, passw: int) -> str:

    # Na "twardo" sprawdzanie danych logowania do testowania makiety
    if user == TEST_USER and passw == TEST_MD5:
        # print("Poprawne logowanie")
        token = int(random.random() * 1000000000)

    return token # zwracanie utworzonego tokenu


"""
Funkcja which_direction służy do sprawdzenia w jakiej odległości jest samochód (o podanym tokenie),
do wyliczenia kierunku w jakim ten samochód ma jechać oraz zwrócenia go.
"""
def which_direction(token: str, distance_cm: int) -> WhereDrive:

    if token == remembered_token:
        return states.stateAction(distance_cm)

    return WhereDrive.ERROR

#####################################################################

app = Flask('serwer')

@app.route('/auth', methods=['POST'])
def authentication():

    data = json.loads(request.data)
    print(data)
    if data["user"] and data["pass"]:

        global remembered_token
        remembered_token = check_authentication(data["user"], data["pass"])

    # Zmienna w jsonie: zmienna w pythonie
    return {"token": remembered_token}

@app.route('/direction', methods=['GET'])
def direction():

    data = json.loads(request.data)
    print(data)
    if data["token"] and data["distance_cm"]:

        turn_direction = which_direction(data["token"], data["distance_cm"])

    # Zmienna w jsonie: zmienna w pythonie
    return {"turn_direction": turn_direction}

app.run()
