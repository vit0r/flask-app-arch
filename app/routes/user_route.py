"""
cop-op marketing user route
"""

from flask import Blueprint
from flask_api import status
from app.modules.user_module import UserModule

user_bp = Blueprint(name='user_bp', import_name=__name__, url_prefix='/api')


@user_bp.route('/users', methods=['GET'])
def find_all():
    users = UserModule().find_all()
    if not users:
        return None, status.HTTP_204_NO_CONTENT
    return {'data': users.data}, status.HTTP_200_OK
