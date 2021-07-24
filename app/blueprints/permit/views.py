from werkzeug.exceptions import abort

from app import db
from flask import Blueprint, request, render_template, current_app, redirect, flash, url_for
from app.blueprints.permit.model.permit import Permit
from app.blueprints.permit.model.permit_area_pollutant import PermitAreaPollutant
from app.constants import CONSTANTS
from app.blueprints.main.model.parish import Parish
from app.blueprints.main.model.town import Town
from app.blueprints.main.model.town_pollutant import TownPollutant
from app.blueprints.main.model.user import User
from app.blueprints.main.model.pollutant import Pollutant
from app.blueprints.permit.form.permit_request import PermitRequestForm
from app.blueprints.main.service.town_service import get_towns
from datetime import datetime


permit = Blueprint("permit", __name__)


@permit.route("new", methods=["GET", "POST"])
def new_permit():
    permit_form = PermitRequestForm(request.form)
    permit_form.parish.choices = [(parish.id, parish.name) for parish in Parish.query.all()]
    if permit_form.parish.data != "default":
        permit_form.town.choices = get_towns(permit_form.parish.data)

    if request.method == "POST" and permit_form.validate():
        permit_header = Permit(area_name=permit_form.area_name.data, square_footage=permit_form.square_footage.data, town_id=permit_form.town.data, user_id=1)
        try:
            db.session.add(permit_header)
            db.session.flush()
            db.session.add(PermitAreaPollutant(permit_id=permit_header.id, pollutant_id=permit_form.AQI.id, pollutant_level=float(permit_form.AQI.data)))
            db.session.add(PermitAreaPollutant(permit_id=permit_header.id, pollutant_id=permit_form.PM25.id, pollutant_level=float(permit_form.PM25.data)))
            db.session.add(PermitAreaPollutant(permit_id=permit_header.id, pollutant_id=permit_form.PM10.id, pollutant_level=float(permit_form.PM10.data)))
            db.session.add(PermitAreaPollutant(permit_id=permit_header.id, pollutant_id=permit_form.CO.id, pollutant_level=float(permit_form.CO.data)))
            db.session.add(PermitAreaPollutant(permit_id=permit_header.id, pollutant_id=permit_form.NO2.id, pollutant_level=float(permit_form.NO2.data)))
            db.session.add(PermitAreaPollutant(permit_id=permit_header.id, pollutant_id=permit_form.SO2.id, pollutant_level=float(permit_form.SO2.data)))
            db.session.add(PermitAreaPollutant(permit_id=permit_header.id, pollutant_id=permit_form.O3.id, pollutant_level=float(permit_form.O3.data)))
            db.session.commit()
            flash("Permit Request Created", "success")
            return redirect(url_for("permit.specific_permit", permit_id=permit_header.id))
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            flash(CONSTANTS["SYSTEM_ERROR_MESSAGE"], "danger")

    if request.method == "POST" and permit_form.parish.data != "default":
        permit_form.town.choices = get_towns(permit_form.parish.data)

    # default choices added after validation so they are not considered as valid options but still displayed
    permit_form.parish.choices.insert(0, ("default", "Choose a Parish"))
    permit_form.town.choices.insert(0, ("default", "Choose a Town"))

    return render_template("new_permit_request.html", permit_form=permit_form,
                           current_date=datetime.now().strftime(current_app.config["DISPLAY_DATE_FORMAT"]))


@permit.route("/<int:permit_id>", methods=["GET", "POST"])
def specific_permit(permit_id):

    display_permit = Permit.query.filter_by(id=permit_id).first()

    if display_permit:
        return render_template('display_permit_request.html', permit=display_permit, requester=display_permit.user,
                               request_date=str(display_permit.created_on.strftime(current_app.config['DISPLAY_DATE_FORMAT'])))

    abort(404)
