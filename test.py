import requests

BASE = "http://127.0.0.1:5001/"

response = requests.get(BASE + "helloworld")
print(response.json())