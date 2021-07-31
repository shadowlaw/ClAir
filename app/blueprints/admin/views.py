from flask import Blueprint, render_template, request
from flask_login import login_required

from app.blueprints.admin.form.pollutant_upload_form import PollutantUploadForm

admin_views = Blueprint('admin_views', __name__)


@admin_views.route('/pollutant/upload', methods=['GET', 'POST'])
@login_required
def upload_pollutant():
    pollutant_upload = PollutantUploadForm()

    if request.method == 'POST' and pollutant_upload.validate():
        pass

    return render_template('pollutant_upload.html', upload_form=pollutant_upload)
