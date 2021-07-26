from werkzeug.exceptions import abort

from app import db
from flask import Blueprint, request, render_template, current_app, redirect, flash, url_for
from app.blueprints.permit.model.planning_application import PlanningApplication
from app.blueprints.permit.model.planning_application_area_pollutant import PlanningApplicationAreaPollutant
from app.constants import CONSTANTS
from app.blueprints.main.model.parish import Parish
from app.blueprints.main.model.town import Town
from app.blueprints.main.model.town_pollutant import TownPollutant
from app.blueprints.main.model.user import User
from app.blueprints.main.model.pollutant import Pollutant
from app.blueprints.permit.form.planning_application import PlanningApplicationForm
from app.blueprints.main.service.town_service import get_towns
from datetime import datetime
from flask_login import login_required


planning_application_views = Blueprint("planning_application_views", __name__)


@planning_application_views.route("new", methods=["GET", "POST"])
@login_required
def new_application():
    planning_application_form = PlanningApplicationForm(request.form)
    planning_application_form.parish.choices = [(parish.id, parish.name) for parish in Parish.query.all()]
    if planning_application_form.parish.data != "default":
        planning_application_form.town.choices = get_towns(planning_application_form.parish.data)

    if request.method == "POST" and planning_application_form.validate():
        application_header = PlanningApplication(area_name=planning_application_form.area_name.data, square_footage=planning_application_form.square_footage.data, town_id=planning_application_form.town.data, user_id=1)
        try:
            db.session.add(application_header)
            db.session.flush()
            db.session.add(PlanningApplicationAreaPollutant(application_id=application_header.id, pollutant_id=planning_application_form.AQI.id, pollutant_level=float(planning_application_form.AQI.data)))
            db.session.add(PlanningApplicationAreaPollutant(application_id=application_header.id, pollutant_id=planning_application_form.PM25.id, pollutant_level=float(planning_application_form.PM25.data)))
            db.session.add(PlanningApplicationAreaPollutant(application_id=application_header.id, pollutant_id=planning_application_form.PM10.id, pollutant_level=float(planning_application_form.PM10.data)))
            db.session.add(PlanningApplicationAreaPollutant(application_id=application_header.id, pollutant_id=planning_application_form.CO.id, pollutant_level=float(planning_application_form.CO.data)))
            db.session.add(PlanningApplicationAreaPollutant(application_id=application_header.id, pollutant_id=planning_application_form.NO2.id, pollutant_level=float(planning_application_form.NO2.data)))
            db.session.add(PlanningApplicationAreaPollutant(application_id=application_header.id, pollutant_id=planning_application_form.SO2.id, pollutant_level=float(planning_application_form.SO2.data)))
            db.session.add(PlanningApplicationAreaPollutant(application_id=application_header.id, pollutant_id=planning_application_form.O3.id, pollutant_level=float(planning_application_form.O3.data)))
            db.session.commit()
            flash("Planning Application Created", "success")
            return redirect(url_for("planning_application_views.specific_application", application_id=application_header.id))
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            flash(CONSTANTS["SYSTEM_ERROR_MESSAGE"], "danger")

    if request.method == "POST" and planning_application_form.parish.data != "default":
        planning_application_form.town.choices = get_towns(planning_application_form.parish.data)

    # default choices added after validation so they are not considered as valid options but still displayed
    planning_application_form.parish.choices.insert(0, ("default", "Choose a Parish"))
    planning_application_form.town.choices.insert(0, ("default", "Choose a Town"))

    return render_template("new_permit_request.html", permit_form=planning_application_form,
                           current_date=datetime.now().strftime(current_app.config["DISPLAY_DATE_FORMAT"]))


@planning_application_views.route("/<int:application_id>", methods=["GET"])
def specific_application(application_id):

    planning_application = PlanningApplication.query.filter_by(id=application_id).first()

    if planning_application:
        return render_template('display_permit_request.html', permit=planning_application, requester=planning_application.user,
                               request_date=str(planning_application.created_on.strftime(current_app.config['DISPLAY_DATE_FORMAT'])))

    abort(404)
