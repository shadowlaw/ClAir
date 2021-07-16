from flask.blueprints import Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return "home page"
