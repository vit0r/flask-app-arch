"""
cop-op marketing user route
"""

from flask import Blueprint
from app.modules.user_module import UserModule
from app.bases.response_wrapper import ResponseWrapper as rw

user_bp = Blueprint(name='user_bp', import_name=__name__, url_prefix='/api')


@user_bp.route('/users', methods=['GET'])
@rw.resp
def find_all():
    users = UserModule().find_all()
    return users.data
