from requests import get, post

firstInt = 1
seconInt = 2

#parameters = {"distance_cm": firstInt, "token": seconInt}
parameters = {"user": firstInt, "pass": seconInt}

#response = get("http://127.0.0.1:5000/direction", json = parameters)
response = post("http://127.0.0.1:5000/auth", json = parameters)

if response.status_code == 200:
    print(response.json())