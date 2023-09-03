#!/usr/bin/env python3

from random import choice as rc
from faker import Faker
from app import app
from models import db, Zookeeper, Animal, Enclosure

fake = Faker()

with app.app_context():

    Animal.query.delete()
    Zookeeper.query.delete()
    Enclosure.query.delete()

    zookeepers = []
    for n in range(25):
        zk = Zookeeper(name=fake.name(), birthday=fake.date_between(start_date='-70y', end_date='-18y'))
        zookeepers.append(zk)
    db.session.add_all(zookeepers)

    enclosures = []
    environments = ['Desert', 'Pond', 'Ocean', 'Field', 'Trees', 'Cave', 'Cage']
    for n in range(25):
        environment = rc(environments)
        print(f"Creating enclosure with environment: {environment}")
        e = Enclosure(environment=environment, open_to_visitors=rc([True, False]))
        enclosures.append(e)
    db.session.add_all(enclosures)

    animals = []
    used_names = set()
    species = ['Lion', 'Tiger', 'Bear', 'Hippo', 'Rhino', 'Elephant', 'Ostrich', 'Snake', 'Monkey']
    for n in range(200):
        name = fake.first_name()
        while name in used_names:
            name = fake.first_name()
        used_names.add(name)
        
        a = Animal(name=name, species=rc(species))
        a.zookeeper = rc(zookeepers)
        a.enclosure = rc(enclosures)
        animals.append(a)
    db.session.add_all(animals)
    
    db.session.commit()
