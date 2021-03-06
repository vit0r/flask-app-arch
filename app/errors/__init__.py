from flask import Blueprint
from flask_api import status

bp = Blueprint(name=__file__, import_name=__name__)


@bp.app_errorhandler(status.HTTP_404_NOT_FOUND)
def not_found_error(error):
    return 'Recurso não encontrando {}\n'.format(error), status.HTTP_404_NOT_FOUND


@bp.app_errorhandler(status.HTTP_500_INTERNAL_SERVER_ERROR)
def internal_error(error):
    return '', status.HTTP_500_INTERNAL_SERVER_ERROR
