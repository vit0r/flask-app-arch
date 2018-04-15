"""
cop-op marketing swagger route
"""

from flask import Blueprint

swagger_bp = Blueprint(name='swagger', import_name=__name__, url_prefix='/api')
