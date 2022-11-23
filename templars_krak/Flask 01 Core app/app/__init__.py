

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# needs the users blueprint
#from flask_login import LoginManager

from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)

# needs the users blueprint
#login = LoginManager(app)
#login.login_view = 'users/login'  # login view if redirection by @login_required

from app import views
# blueprints
#from .users import users
#app.register_blueprint(users, url_prefix="/users")


# needs the admin blueprint
#from . import admin
