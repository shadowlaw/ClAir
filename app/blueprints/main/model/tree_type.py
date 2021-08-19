from app import db


class TreeType(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
