from app import db
from app import create_app
from app.blueprints.main.model.parish import Parish
from app.blueprints.main.model.town import Town
import csv

from app.blueprints.main.model.user import User

app = create_app()


def read_parish_data():
    with open('data/jamaican_towns.csv', mode='r', newline='', encoding='UTF-8') as town_file:
        return list(csv.DictReader(town_file, delimiter=',', quotechar='"'))


def load_parish_town_data(town_data):
    print("Populating Parish and Towns")
    parishes_seen = []
    towns_seen = []
    with app.app_context():
        for row in town_data:
            parish_name = row['Parish']
            parish_id = 'ST_'+parish_name.split(" ")[1][:3].upper() if 'saint' in parish_name.lower() else parish_name.split()[0][:3].upper()
            town_name = row['Town']
            town_id = town_name[:3].upper().replace(" ", "")+town_name[-3:].upper().replace(" ", "")

            if parish_name not in parishes_seen:
                parish = Parish(id=parish_id, name=parish_name)
                db.session.add(parish)
                parishes_seen.append(parish_name)

            if town_name not in towns_seen:
                town = Town(id=town_id, parish_id=parish_id, name=town_name)
                db.session.add(town)
                towns_seen.append(town_name)

            db.session.commit()
    print("Done")


def add_default_user():
    print("Creating default user")
    with app.app_context():
        db.session.add(User(username='default', password='pbkdf2:sha256:150000$GjuQgVkr$003437af92ded1a1d99ebcc56bf20d9bc4dd03e471380aa73c2a7a15a9321194'))
        db.session.commit()
    print("Done")


if __name__ == "__main__":
    data = read_parish_data()
    load_parish_town_data(data)
    add_default_user()
