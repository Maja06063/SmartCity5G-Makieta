from flask import Flask, request
import json

# Enum kierunków ruchu:
class WhereDrive():

    GO_LEFT = 1
    GO_RIGHT = 2
    GO_STRAIGHT = 3
    DESTINATION = 4

"""
Funkcja check_authentication służy do sprawdzenia czy samochód przesłał
poprawny login i hasło i jeśli tak, do wygenerowania i zachowania na potem tokenu.
"""
def check_authentication(user: str, passw: int) -> str:

    #Tu ma być kod, który wylicza token (Ola)
    return "123" # placeholder

"""
Funkcja which_direction służy do sprawdzenia w jakiej odległości jest samochód (o podanym tokenie),
do wyliczenia kierunku w jakim ten samochód ma jechać oraz zwrócenia go.
"""
def which_direction(token: str, distance_cm: int) -> WhereDrive:

    # Tu ma być kod do zamiany dystansu na kierunek (Ola)
    return WhereDrive.GO_STRAIGHT

app = Flask('serwer')

@app.route('/auth', methods=['POST'])
def authentication():

    data = json.loads(request.data)
    if data["user"] and data["pass"]:


        token = check_authentication(data["user"], data["pass"])

    # Zmienna w jsonie: zmienna w pythonie
    return {"token": token}

@app.route('/direction', methods=['GET'])
def direction():

    data = json.loads(request.data)
    if data["token"] and data["distance_cm"]:

        turn_direction = which_direction(data["token"], data["distance_cm"])

    # Zmienna w jsonie: zmienna w pythonie
    return {"turn_direction": turn_direction}

app.run()