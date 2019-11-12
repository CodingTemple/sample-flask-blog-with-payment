from flask import Flask

# Config imports 
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

# Import for Flask Login

from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)

#Login Flow config
login = LoginManager(app)
login.login_view = 'login' # This specifices what page to laod for non-authed users


from nonprofitorg import routes, models 