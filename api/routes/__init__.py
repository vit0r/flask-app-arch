"""
cop-op marketing base route
"""

from flask import Blueprint

base_bp = Blueprint(name='base_bp', import_name=__name__)


@base_bp.route('/', methods=['GET'])
def home():
    return '<b>Works</b>'
