import csv
from io import TextIOWrapper
from app import db
from datetime import datetime

from flask import Blueprint, render_template, request, current_app, flash
from flask_login import login_required

from app.blueprints.admin.exception.UnsupportedFieldException import UnsupportedFieldException
from app.blueprints.admin.form.air_quality_upload_form import AirQualityUploadForm
from app.blueprints.admin.utils.wrappers import admin_role_required
from app.blueprints.main.model.pollutant import Pollutant
from app.blueprints.main.model.town import Town
from app.blueprints.main.model.town_pollutant import TownPollutant

admin_views = Blueprint('admin_views', __name__)


@admin_views.route('/air_quality/upload', methods=['GET', 'POST'])
@admin_role_required
@login_required
def air_quality_upload():
    aq_upload = AirQualityUploadForm()

    if request.method == 'POST' and aq_upload.validate():
        aq_upload.file.data.stream.seek(0)
        csv_data = csv.DictReader(TextIOWrapper(aq_upload.file.data), delimiter=',', quotechar='"')
        pollutants = [pollutant.id for pollutant in Pollutant.query.all()]
        file_pollutant = csv_data.fieldnames[2:]
        upload_complete = False
        message = 'Upload Failed. No data in file'
        category = 'warning'

        for row in csv_data:
            town = Town.query.filter_by(id=row['Town ID']).first()

            if town:
                try:
                    for key in file_pollutant:
                        if key not in pollutants:
                            error = 'Pollutant %s is not supported by the system' % key
                            raise UnsupportedFieldException(error)

                        db.session.add(TownPollutant(town_id=town.id,
                                                     collection_date=datetime.strptime(row['Date'], '%m/%d/%Y'),
                                                     pollutant_id=key, pollutant_level=row[key]))
                    db.session.commit()

                except Exception as e:
                    db.session.rollback()
                    current_app.logger.error(e)
                    flash(e, 'danger')
                    break
                flash('Air Quality Upload Complete', 'success')
            else:
                flash('Town %s does not exist' % row['Town ID'])
                break

        if upload_complete:
            message = 'Upload Failed Successful'
            category = 'success'

        flash(message, category)

    return render_template('air_quality_upload.html', upload_form=aq_upload)
