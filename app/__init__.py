from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Необходимо авторизоваться!'
login_manager.login_message_category = 'alert-warning'
db = SQLAlchemy(app)

from . import models, views  # noqa

db.create_all()
