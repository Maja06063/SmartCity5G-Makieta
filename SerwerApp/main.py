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

    # Na "twardo" sprawdzanie danych logowania do testowania makiety
    if user == 1 and passw == 266003691477286198901011725417809479212:
        # print("Poprawne logowanie")
        token = {"Authorization": "Bearer TokenForExperiments"} # Tworzenie tokenu ?

    return token # zwracanie utworzonego tokenu

# Obszar globalny na zmienne globalne do funkcji poniżej
#going_straight = 1
#before_turn_left = 2
#after_turn_left = 3
#before_turn_right = 4
#after_turn_right = 5
#on_destination = 6
my_state = 'prosto'    # stan w jakim jest samochód (na początku jedzie prosto)
iter_turn = 0

"""
Funkcja which_direction służy do sprawdzenia w jakiej odległości jest samochód (o podanym tokenie),
do wyliczenia kierunku w jakim ten samochód ma jechać oraz zwrócenia go.
"""
def which_direction(token: str, distance_cm: int) -> WhereDrive:

    # Tu ma być kod do zamiany dystansu na kierunek (Ola)
    # zapamietanie w jakies zmiennej globalnej ostatni stan (duzo ifow mnie czeka i ify w ifach )
    # stany: jedzie prosto, skret (przed i po), docelowe miejsce 
    #my_state = 1 # stan w jakim jest samochód (na początku jedzie prosto)
    d_max = 10  # odleglosc od sciany, przy ktorym skret, moze sie zmienic - potrzebne wymiary fizyczne makiety
    d_destination = 40 # wstepnie założę, że miejsce parkingowe będzie 40 cm od ściany

    if my_state == 'prosto':
        if distance_cm <= d_max:
            my_state = 'przed skretem'
        if distance_cm > d_max:
            return WhereDrive.GO_STRAIGHT
        
    if iter_turn == 0 or iter_turn == 1: # Jak trasa na szkicach to skrety w lewo sa dwa pierwszy i drugi skret
        if my_state == 'przed skretem':
            my_state = 'po skrecie'
            iter_turn = iter_turn + 1
            return WhereDrive.GO_LEFT
    
    if iter_turn == 2 and distance_cm <= d_destination: # Jak trasa na szkicach to skret w prawo jest na miejsce parkingowe
        if my_state == 'przed skretem':
            my_state = 'na miejscu'
            iter_turn = iter_turn + 1
            return WhereDrive.GO_RIGHT

    if my_state == 'po skrecie':
        if distance_cm > d_max:
            my_state = 'prosto'
            return WhereDrive.GO_STRAIGHT
    if my_state == 'na miejscu':
        return WhereDrive.DESTINATION

    # if distance_cm > d_max:
        # return WhereDrive.GO_STRAIGHT
    # if distance_cm <= d_max:
        # skad wiadomo czy ma skrecic w lewo czy w prawo ? tez kinda na twardo (ja wybieram konkretne miejsce i trase)
        # return WhereDrive.GO_LEFT
    # jaki if na wiedzenie czy jest na miejscu ? 
    
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