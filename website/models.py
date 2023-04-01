from . import db
import uuid
from flask_login import UserMixin


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    date = db.Column(db.DateTime)
    color = db.Column(db.String(35))
    user_name = db.Column(db.String(35))
    data = db.Column(db.String(400))
