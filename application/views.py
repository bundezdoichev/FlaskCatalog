from flask import Flask, render_template_string, render_template, redirect, request, url_for, Blueprint
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager
from flask_login.utils import current_user, login_user, logout_user

from .models import User
from .forms import LoginForm
from .extentions import db, bcrypt

views = Blueprint('views', __name__, template_folder="templates")

# we don't need to access config here, so keep it empty (otherwise "blueprint 
# has no attribute 'config' error given")
views.config = {}


class ItemView(ModelView):
    column_filters = ['color', 'weight', 'price', 'city']


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.is_admin
        else:
            return False




@views.route('/home', methods=['GET'])
def home():
    return render_template_string('Home page!')


@views.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('views.home'))
        else:
            return render_template('login.html', form=LoginForm())
    elif request.method == 'POST':
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user:
                if bcrypt.check_password_hash(user.password, form.password.data):
                    login_user(user)
                    return redirect(url_for('views.home'))
                else:
                    form.email.errors.append('Wrong email or password')
                    return render_template('login.html', form=form)
                    
            else:
                return render_template('login.html', form=form)
        else:
            return render_template('login.html', form=form)


@views.route('/logout', methods=['GET'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('views.home'))
    else:
        return redirect(url_for('views.home'))


