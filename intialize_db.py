from app import db
from app import create_app
from app.blueprints.main.model.parish import Parish
from app.blueprints.main.model.town import Town
from app.blueprints.main.model.tree import Tree
from app.blueprints.main.model.tree_efficacy import TreeEfficacy
import csv

from app.blueprints.main.model.tree_type import TreeType
from app.blueprints.main.model.user import User

app = create_app()


def read_csv_file(filename):
    with open(filename, mode='r', newline='', encoding='UTF-8') as file_ptr:
        return list(csv.DictReader(file_ptr, delimiter=',', quotechar='"'))


def load_parish_town_data():
    print("Populating Parish and Towns")
    town_data = read_csv_file('data/jamaican_towns.csv')
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
                town = Town(id=town_id, parish_id=parish_id, name=town_name, size=row['sq. ft.'])
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


def populate_trees():
    print("Populating Trees and efficacy against pollutants")
    with app.app_context():
        tree_data = read_csv_file('data/compiled_tree_file.csv')
        pollutants = {
            'Carbon Monoxide': 'CO', 'Nitrogen Dioxide': 'NO2', 'Sulfur Dioxide': 'SO2',
            'Ozone': 'O3', 'Particulate Matter': 'PM'
        }

        seen_types = []

        for row in tree_data:
            tree_id = row['Scientic Name'].split()[0][:3]+row['Scientic Name'].split()[1][:3]
            type_name = row['Scientic Name'].split()[0]
            type_id = type_name[:3]

            if type_name not in seen_types:
                seen_types.append(type_name)
                db.session.add(
                    TreeType(id=type_id, name=type_name)
                )

            db.session.add(
                Tree(id=tree_id, name=row['Common Name'], maturity_size=row['Max height of tree (feet)'],
                     space_required=row['Crown Diameter (feet)'], type_id=type_id)
            )

            for key in row.keys():
                if key in pollutants.keys():
                    if key == 'Particulate Matter':
                        db.session.add(
                            TreeEfficacy(tree_id=tree_id, pollutant_id=str(pollutants[key])+'10', effectiveness=row[key])
                        )
                        db.session.add(
                            TreeEfficacy(tree_id=tree_id, pollutant_id=str(pollutants[key])+'25', effectiveness=row[key])
                        )
                    else:
                        db.session.add(
                            TreeEfficacy(tree_id=tree_id, pollutant_id=pollutants[key], effectiveness=row[key])
                        )

            db.session.commit()
        print('Done')


if __name__ == "__main__":
    load_parish_town_data()
    add_default_user()
    populate_trees()
