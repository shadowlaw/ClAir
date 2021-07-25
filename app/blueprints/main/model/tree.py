from app import db

class Tree(db.Model):

    id = db.Column(db.String(100),  primary_key=True)
    name = db.Column(db.String(255),  nullable=False)
    maturity_size = db.Column(db.Numeric(precision=2), nullable=False)
    space_required = db.Column(db.Numeric(precision=2), nullable=False)
