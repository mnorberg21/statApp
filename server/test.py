import requests

BASE = "http://127.0.0.1:5001/"
# BASE = "http://172.17.0.3:5001/"

response = requests.get(BASE + "helloworld")
print(response.json())