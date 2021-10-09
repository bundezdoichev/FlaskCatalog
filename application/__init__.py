from flask import Flask, Blueprint
from flask_basicauth import BasicAuth
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin

from .models import User, Item, City
from .views import MyAdminIndexView, ItemView, ModelView, views
from .extentions import db


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.register_blueprint(views)

admin = Admin(app, index_view=MyAdminIndexView())
admin.add_view(ItemView(Item, db.session))
admin.add_view(ModelView(City, db.session))

basic_auth = BasicAuth(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

