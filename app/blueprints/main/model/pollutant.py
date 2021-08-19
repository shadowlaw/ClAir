from app import db


class Pollutant(db.Model):

    id = db.Column(db.String(100),  primary_key=True)
    name = db.Column(db.String(255),  nullable=False)
    safe_level = db.Column(db.Numeric(), nullable=False)
