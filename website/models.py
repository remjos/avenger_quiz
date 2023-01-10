from . import db 
from flask_login import UserMixin 
from sqlalchemy.sql import func 

class Note(db.model):
    id = db.Column(db.Integer, primarykey=True)
    data = db.Column(db.string(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) 
    user_id = db.Column(db.integer, db.ForeignKey('user.id'))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) 
    password = db.Column(db.String(150))
    first_name = db.Column(db.string(150)) 
    notes = db.relationship('Note') 
    
