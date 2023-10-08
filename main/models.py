from main import db


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file = db.Column(db.String(128), nullable=False)
    column = db.Column(db.String(128), nullable=False)
    