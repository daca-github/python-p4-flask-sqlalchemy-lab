from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, default='Unnamed')
    species = db.Column(db.String(50), nullable=False, default='Unknown')
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeeper.id'), nullable=False)
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosure.id'), nullable=False)

class Zookeeper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, default='Unnamed')
    birthday = db.Column(db.Date, nullable=False, default=date.today())
    animals = db.relationship('Animal', backref='zookeeper')

class Enclosure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(50), nullable=False)
    open_to_visitors = db.Column(db.Boolean, default=True)
    animals = db.relationship('Animal', backref='enclosure')
