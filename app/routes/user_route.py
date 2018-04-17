"""
cop-op marketing user route
"""

from flask import Blueprint, request
from app.modules.user_module import UserModule
from app.bases.response_wrapper import ResponseWrapper as rw

user_bp = Blueprint(name='user_bp', import_name=__name__, url_prefix='/api')


@user_bp.route('/users', methods=['GET'])
@rw.resp
def find_all():
    users = UserModule().find_all()
    return users.data


@user_bp.route('/user', methods=['POST'])
@rw.resp
def create():
    user_payload = request.get_json()
    UserModule().create(user_payload)
