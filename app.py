from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.plant import Plant, PlantList
from resources.genus import Genus, GenusList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'testKey'
api = Api(app)

@app.before_first_request
def create_tables():
	db.create_all()

jwt = JWT(app, authenticate, identity) # /auth  end point

api.add_resource(Genus, '/genus/<string:name>')
api.add_resource(Plant, '/plant/<string:name>')
api.add_resource(PlantList, '/plants')
api.add_resource(UserRegister, '/register')
api.add_resource(GenusList, '/genera')


if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(port=5000, debug=True)
