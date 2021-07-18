from flask import Blueprint, request, render_template
from app.model.parish import Parish
from app.model.town import Town
from app.blueprints.permit.form.permit_request import PermitRequestForm


permit = Blueprint("permit", __name__)


@permit.route("new", methods=["GET", "POST"])
def new_permit():
    permit_form = PermitRequestForm(request.form)
    permit_form.parish.choices = [(parish.id, parish.name) for parish in Parish.query.all()]
    if permit_form.parish.data != "default":
        permit_form.town.choices = [(town.id, town.name) for town in Town.query.filter_by(parish_id=permit_form.parish.data).all()]

    if request.method == "POST" and permit_form.validate():
        pass

    # default choices added after validation so they are not considered as valid options but still displayed
    permit_form.parish.choices.insert(0, ("default", "Choose a Parish"))
    permit_form.town.choices = [("default", "Choose a Town")]

    return render_template("new_permit_request.html", permit_form=permit_form)
