from flask import Blueprint, render_template, current_app
from flask_login import login_required
from werkzeug.exceptions import abort

from app.blueprints.main.model.tree_efficacy import TreeEfficacy
from app.blueprints.report.model.report import Report

report_views = Blueprint('report_views', __name__)


@report_views.route('/<int:report_id>')
@login_required
def specific_report(report_id):
    report = Report.query.filter_by(id=report_id).first()
    if report:
        for report_detail in report.report_details:
            report_detail.targeted_pollutant_tree_efficacy = \
                TreeEfficacy.query.filter_by(pollutant_id=report_detail.targeted_pollutant,
                                             tree_id=report_detail.tree_id).first()
        return render_template("report.html", report=report, created_on=report.created_on.strftime(current_app.config['DISPLAY_DATE_FORMAT']))

    current_app.logger.warn("Unable to locate report with id: %d" % report_id)
    abort(404)
