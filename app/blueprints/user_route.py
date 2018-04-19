from flask import Blueprint, request
from app.modules.user_module import UserModule
from app.libraries.response_wrapper import ResponseWrapper as rw

bp = Blueprint(name=__file__, import_name=__name__)


@bp.route('/users/', methods=['GET'])
@rw.resp
def find_all():
    users = UserModule().find_all()
    return users.data


@bp.route('/user/<username>/', methods=['GET'], endpoint='user_name')
@rw.resp
def find(username=None):
    users = UserModule().find(username)
    return users.data


@bp.route('/user/', methods=['POST'], endpoint='create_user')
@rw.resp
def create():
    user_payload = request.get_json()
    UserModule().create(user_payload)
