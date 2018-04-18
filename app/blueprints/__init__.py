"""
cop-op marketing Blueprint
"""

from flask import Blueprint

bp = Blueprint(name=__file__, import_name=__name__)


@bp.route('/', methods=['GET'], endpoint='home')
def home():
    return '<b>{}</b>'.format(__file__)
