from requests import get, post

firstInt = 1
seconInt = 2

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