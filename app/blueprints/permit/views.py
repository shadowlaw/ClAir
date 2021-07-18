from flask import Blueprint, request, render_template
from app.model.parish import Parish
from app.model.town import Town
from app.blueprints.permit.form.permit_request import PermitRequestForm
from app.service.town_service import get_towns

permit = Blueprint("permit", __name__)


@permit.route("new", methods=["GET", "POST"])
def new_permit():
    permit_form = PermitRequestForm(request.form)
    permit_form.parish.choices = [(parish.id, parish.name) for parish in Parish.query.all()]
    if permit_form.parish.data != "default":
        permit_form.town.choices = get_towns(permit_form.parish.data)

    if request.method == "POST" and permit_form.validate():
        pass
    if request.method == "POST" and permit_form.parish.data != "default":
        permit_form.town.choices = get_towns(permit_form.parish.data)

    # default choices added after validation so they are not considered as valid options but still displayed
    permit_form.parish.choices.insert(0, ("default", "Choose a Parish"))
    permit_form.town.choices.insert(0, ("default", "Choose a Town"))

    return render_template("new_permit_request.html", permit_form=permit_form)
