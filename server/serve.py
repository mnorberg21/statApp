import pandas as pd
from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
CORS(app)

df = pd.DataFrame({
    'date': ['8/5/2022', '8/6/2022'],
    'course': ['Winchester Country Club', 'Eastward Ho!'],
    'score': ['75', '77'],
    'fairways': ['11', '15'],
    'greens': ['14', '12'],
    'threePutts': ['0', '1'],
})

class HelloWorld(Resource):
    def get(self):
        return {'greeting': 'Hello World'}

class Stats(Resource):
    def get(self):
        return {'total': df.shape[0]}

rest_parser = reqparse.RequestParser()
rest_parser.add_argument('date', type=str)
rest_parser.add_argument('course', type=str)
rest_parser.add_argument('score', type=str)
rest_parser.add_argument('fairways', type=str)
rest_parser.add_argument('greens', type=str)
rest_parser.add_argument('threePutts', type=str)

class Rest(Resource):
    def get(self):
        return df.to_dict(orient = 'records')
    
    def post(self):
        args = rest_parser.parse_args()
        df.loc[len(df.index)] = args
        return {'status': 'data item posted'}

api.add_resource(HelloWorld, "/helloworld")
api.add_resource(Stats, "/stats")
api.add_resource(Rest, "/rest")

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