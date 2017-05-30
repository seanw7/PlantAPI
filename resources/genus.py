from flask_restful import Resource
from models.genus import GenusModel

from flask_jwt import jwt_required

class Genus(Resource):

    @jwt_required()
    def get(self, name):
        genus = GenusModel.find_by_name(name)
        if genus:
            return genus.json()
        return {'message': 'Genus not found'}, 404

    @jwt_required()
    def post(self, name):
        genus = GenusModel.find_by_name(name)
        if genus:
            return {'message': "Genus with name '{}' already exists".format(name)}, 400

        genus = GenusModel(name)
        try:
            genus.save_to_db()
        except:
            return {'message': 'An error occurred while creating the genus.'}, 500

        return genus.json(), 201

    @jwt_required()
    def delete(self, name):
        genus = GenusModel.find_by_name(name)
        if genus:
            genus.delete_from_db()

        return {'message': 'Genus deleted'}


class GenusList(Resource):
    
    @jwt_required()
    def get(self):
        return {'genera': [genus.json() for genus in GenusModel.query.all()]}
