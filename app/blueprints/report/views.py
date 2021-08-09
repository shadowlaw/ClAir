from flask import Blueprint, render_template, current_app
from werkzeug.exceptions import abort

from app.blueprints.main.model.tree_efficacy import TreeEfficacy
from app.blueprints.report.model.report import Report
from app.blueprints.report.model.targeted_pollutants import TargetedPollutant

report_views = Blueprint('report_views', __name__)


@report_views.route('/<int:report_id>')
def specific_report(report_id):
    report = Report.query.filter_by(id=report_id).first()
    if report:
        for report_detail in report.report_details:
            report_detail.targeted_pollutant_tree_efficacy = \
                TreeEfficacy.query.filter_by(pollutant_id=report_detail.targeted_pollutant,
                                             tree_id=report_detail.tree_id).first()

            report_detail.secondary_pollutants = TargetedPollutant.query.filter_by(report_id=report.id,
                                                                                    tree_id=report_detail.tree_id).all()

            for sec_pol in report_detail.secondary_pollutants:
                sec_pol.tree_efficacy = TreeEfficacy.query.filter_by(pollutant_id=sec_pol.targeted_pollutant_id,
                                                                     tree_id=sec_pol.tree_id).first()

        return render_template("report.html", report=report, created_on=report.created_on.strftime(current_app.config['DISPLAY_DATE_FORMAT']))

    current_app.logger.warn("Unable to locate report with id: %d" % report_id)
    abort(404)
