from app import db

class TreeEfficacy(db.Model):
    
    tree_id = db.Column(db.String(100), db.ForeignKey("tree.id"), primary_key=True)
    pollutant_id = db.Column(db.String(100), db.ForeignKey("pollutant.id"), primary_key=True)
    effectiveness = db.Column(db.Numeric(), nullable=False)
