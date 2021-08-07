from functools import wraps
from flask_login import current_user
from werkzeug.exceptions import abort

from app.blueprints.main.model.user_role import UserRole


def admin_role_required(func):
    @wraps(func)
    def wrapper(*args, **kwds):

        if current_user.is_authenticated and current_user.role == UserRole.ADMIN.value:
            return func(*args, **kwds)

        abort(403)

    return wrapper
