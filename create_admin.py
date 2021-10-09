from application.extentions import db, bcrypt
from application import app
from application.models import User
import os


with app.app_context():
    pasw = os.getenv('ADMIN_PSWD')
    db.init_app(app)
    db.create_all()
    usr = User(email='yuri.korol.0505@gmail.com', password=bcrypt.generate_password_hash(pasw).decode('utf-8'), is_admin=True)
    db.session.add(usr)
    db.session.commit()
