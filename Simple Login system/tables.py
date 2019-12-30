from flask_sqlalchemy import SQLAlchemy
from main import app
from flask_login import UserMixin

db = SQLAlchemy(app)

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)