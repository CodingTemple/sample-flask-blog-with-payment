'''
    Models.py is where we will create our database "tables" AKA models.
    which are python Objects that will be mapped to tables when a migration 
    happens.

    - Migration: Taking a Object in pyhton(AKA class) relating that object to 
    SQL code that is written from our python code.
'''

from flask_sqlalchemy import SQLAlchemy
from nonprofitorg import app,db
from werkzeug.security import generate_password_hash,check_password_hash

# import for Date Time 
from datetime import datetime

# User Auth Flow Mixin
from flask_login import UserMixin

# Import login_manager 
from nonprofitorg import login

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# One to Many Relationship
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String(256), nullable = False)
    post = db.relationship('Post', backref = 'author', lazy = True)

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def __repr__(self):
        return '{} has been created'.format(self.username)

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False)

    def __repr__(self):
        return "The Title is {} and the user is {}".format(self.titel,self.user_id)


# USER ID => 1

#POST_ID: 23 => Created by USER_ID: 1

