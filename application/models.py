from flask_login import UserMixin
from .extentions import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


# creating ManyToMany relation in order to filter items by city field
table = db.Table('item-location',
    db.Column('item_id', db.Integer, db.ForeignKey('items.id')),
    db.Column('city_id', db.Integer, db.ForeignKey('cities.id')),   
)


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(25), nullable=False)
    weight = db.Column(db.Float)
    price = db.Column(db.Float)
    city = db.relationship('City', 
            secondary=table, 
            backref=db.backref('items', lazy='dynamic')
    )


class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)

