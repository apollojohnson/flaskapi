from app import db
from datetime import datetime


class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Float())
    image = db.Column(db.String())
    description = db.Column(db.String())
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)

# initialize it
    def __init__(self, name, price, image, description):
        self.name = name
        self.price = price
        self.image = image
        self.description = description


# to send it back as a json response:
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'image': self.image,
            'description': self.description,
            'created_on': self.created_on
        }