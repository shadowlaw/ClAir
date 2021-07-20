from app import db
from app import create_app
from app.blueprints.main.model.parish import Parish
from app.blueprints.main.model.town import Town
import csv

app = create_app()


def read_parish_data():
    with open('data/jamaican_towns.csv', mode='r', newline='', encoding='UTF-8') as town_file:
        return list(csv.DictReader(town_file, delimiter=',', quotechar='"'))


def load_parish_town_data(town_data):
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


if __name__ == "__main__":
    data = read_parish_data()
    load_parish_town_data(data)
