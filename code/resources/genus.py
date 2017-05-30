from flask_restful import Resource
from models.genus import GenusModel

class Genus(Resource):
    def get(self, name):
        genus = GenusModel.find_by_name(name)
        if genus:
            return genus.json()
        return {'message': 'Genus not found'}, 404

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

    def delete(self, name):
        genus = GenusModel.find_by_name(name)
        if genus:
            genus.delete_from_db()

        return {'message': 'Genus deleted'}


class GenusList(Resource):
    def get(self):
        return {'genera': [genus.json() for genus in GenusModel.query.all()]}
