from flask import Flask, request
import json

class WhereDrive():

    GO_LEFT = 1
    GO_RIGHT = 2
    GO_STRAIGHT = 3
    DESTINATION = 4

app = Flask('serwer')

@app.route('/direction', methods=['GET'])
def direction():
    
    data = json.loads(request.data)
    if data["token"] and data["distance_cm"]:
        
       #Tu ma być funkcja do zamiany dystansu na kierunek (Ola)
        turn_direction = WhereDrive.GO_STRAIGHT # ona ma zwracac turn_direction

            #zmienna w jsonie: w pythonie
    return {"turn_direction": turn_direction}

@app.route('/auth', methods=['POST'])
def authentication():
    
    data = json.loads(request.data)
    if data["user"] and data["pass"]:
        
       #Tu ma być funkcja, która wylicza token (Ola)
        token = 0 # ona ma  token

            #zmienna w jsonie: w pythonie
    return {"token": token}

app.run()