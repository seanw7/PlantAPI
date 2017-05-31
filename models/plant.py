# copied from item.py
from db import db


class PlantModel(db.Model):
    __tablename__ = "plants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    quantity = db.Column(db.Float(precision=2))
    price = db.Column(db.Float(precision=2))

    genus_id = db.Column(db.String(80), db.ForeignKey('genus.name'))
    genus = db.relationship('GenusModel')

    def __init__(self, name, quantity, price, genus_id, url):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.genus_id = genus_id
        self.url = "http://www.palmpedia.net/wiki/{}_{}".format(self.genus_id, self.name)

    def json(self):
        return {"name": self.name, "price": self.price, "quantity": self.quantity, "value": self.quantity * self.price, \
        "url": {self.url}}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
