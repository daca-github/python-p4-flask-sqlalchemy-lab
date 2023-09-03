#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()
    if animal:
        return f"<ul>Name: <li>{animal.name}</li></ul><ul>Species: <li>{animal.species}</li></ul><ul>Zookeeper: <li>{animal.zookeeper.name}</li></ul><ul>Enclosure: <li>{animal.enclosure.environment}</li></ul>"
    else:
        return make_response("Animal not found", 404)

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    if zookeeper:
        animal_names = "<li>".join([animal.name for animal in zookeeper.animals])
        return f"<ul>Name: <li>{zookeeper.name}</li></ul><ul>Birthday: <li>{zookeeper.birthday}</li></ul><ul>Animals: <li>{animal_names}</li></ul>"
    else:
        return make_response("Zookeeper not found", 404)

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    if enclosure:
        animal_names = "<li>".join([animal.name for animal in enclosure.animals])
        return f"<ul>Environment: <li>{enclosure.environment}</li></ul><ul>Open to Visitors: <li>{enclosure.open_to_visitors}</li></ul><ul>Animals: <li>{animal_names}</li></ul>"
    else:
        return make_response("Enclosure not found", 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
