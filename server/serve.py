
import os
from json import dumps
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mnpwd@db:5432/'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
CORS(app)

class scoreModel(db.Model):
    __tablename__ = 'stats'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date())
    course = db.Column(db.String())
    score = db.Column(db.Integer())
    fairways = db.Column(db.Integer())
    gir = db.Column(db.Integer())
    threep = db.Column(db.Integer())

    def __init__(self, date, course, score, fairways, gir, threep):
        self.date = date
        self.course = course
        self.score = score
        self.fairways = fairways
        self.gir = gir
        self.threep = threep
    
    def __repr__(self):
        return f"<Course {self.id}>"

class HelloWorld(Resource):
    def get(self):
        stats = scoreModel.query.all()
        results = [
            {
                "date": stat.date.strftime("%m/%d/%Y"),
                "course": stat.course,
                "score": stat.score,
                "fairways": stat.fairways,
                "gir": stat.gir,
                "threep": stat.threep
            } for stat in stats]
        return {"count": len(results), "stats": results, "message":"success"}

rest_parser = reqparse.RequestParser()
rest_parser.add_argument('id', type=int)
rest_parser.add_argument('date', type=str)
rest_parser.add_argument('course', type=str)
rest_parser.add_argument('score', type=str)
rest_parser.add_argument('fairways', type=str)
rest_parser.add_argument('gir', type=str)
rest_parser.add_argument('threep', type=str)

class Rest(Resource):
    def get(self):
        stats = scoreModel.query.all()
        results = [
            {
                "date": stat.date.strftime("%m/%d/%Y"),
                "course": stat.course,
                "score": stat.score,
                "fairways": stat.fairways,
                "gir": stat.gir,
                "threep": stat.threep
            } for stat in stats]
        return {"count": len(results), "stats": results, "message":"success"}
    
    def post(self):
        args = rest_parser.parse_args()
        new_stat = scoreModel(date = args['date'], course = args['course'], score = args['score'], fairways = args['fairways'], gir = args['gir'], threep = args['threep'])
        print('TEST')
        print(new_stat)
        new_stat.id = args['id']
        db.session.add(new_stat)
        db.session.commit()
        return {'status': 'data item posted'}

api.add_resource(HelloWorld, "/helloworld")
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