from flask import Blueprint, render_template, request
from flask_login import login_required

from app.blueprints.admin.form.air_quality_upload_form import AirQualityUploadForm

admin_views = Blueprint('admin_views', __name__)


@admin_views.route('/air_quality/upload', methods=['GET', 'POST'])
# add role restriction
@login_required
def air_quality_upload():
    aq_upload = AirQualityUploadForm()

    if request.method == 'POST' and aq_upload.validate():
        pass

    return render_template('air_quality_upload.html', upload_form=aq_upload)
