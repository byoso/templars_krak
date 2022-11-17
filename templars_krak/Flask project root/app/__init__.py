import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'  # login view if redirection by @login_required

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import views, models  # this 'app' refers to the package
from app.users import views, models
