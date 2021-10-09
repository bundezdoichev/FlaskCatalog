from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()


# to be imported into run.py and executed with given app instance
def register_extentions(app):
    db.init_app(app)
    bcrypt.init_app(app)

