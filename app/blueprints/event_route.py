"""
cop-op marketing Blueprint
"""

from flask import Blueprint

bp = Blueprint(name=__file__, import_name=__name__)


@bp.route('/events/', methods=['GET'], endpoint='events')
def events():
    return '<b>{}</b>'.format(__file__)
