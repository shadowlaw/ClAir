from flask.blueprints import Blueprint
from flask import render_template, request, flash, redirect, url_for
from app.blueprints.main.form.login import Login
from app.blueprints.main.model.user import User
from app import login_manager
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

main = Blueprint("main", __name__)


@main.route("/")
@login_required
def home():
    return render_template("dashboard.html")

@main.route("/login", methods = ['GET', 'POST'])
def login():
    form = Login()
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username = form.username.data).first()
        if user is not None and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash ('You have been logged in!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash ('Login Unsuccessful. Check username and password', 'danger')

    return render_template("login.html", form = form)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out', 'success')
    return redirect(url_for("main.login"))

