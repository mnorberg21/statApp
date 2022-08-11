from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
CORS(app)

class HelloWorld(Resource):
    def get(self):
        return {'greeting': 'Hello World'}

api.add_resource(HelloWorld, "/helloworld")

if __name__ == "__main__":
    app.run(debug=True, port = 5001, host = "0.0.0.0")

'''
Commands:
docker run -it --name statServer -v ~/Documents/statProject/server:/home/project -p 5001:5001 alpine:3.16
apk update && apk upgrade --available 
apk add --update python3
apk add py3-pip
pip3 install flask flask-restful
flask --app serve run -p 5001 -h 0.0.0.0
'''