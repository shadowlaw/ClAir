from flask.blueprints import Blueprint
from flask import render_template, request


main = Blueprint("main", __name__)


@main.route("/")
def home():
    return "home page"

@main.route("/login", methods = ['GET', 'POST'])
def login():
    return render_template("login.html")
    if request.method == 'POST' and form.validate():
        if form.username == 'billybob' and form.password == 'help':
            flash ('You have been logged in!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            return render_template('login.html', title = 'Login', form = form)



