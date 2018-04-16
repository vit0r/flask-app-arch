"""
cop-op marketing
"""

from os import path
from flask_api import FlaskAPI
from app.bases import db, env, base_schema
from app.errors import errors_bp
from app.routes import base_bp
from app.routes.user_route import user_bp
from app.bases.response_wrapper import ResponseWrapper as rw

__author__ = 'Vitor Nascimento de Araujo'

__instance_path = path.join(path.dirname(__file__), 'instances', env + '.json')
app = FlaskAPI(__name__, instance_path=__instance_path, instance_relative_config=True)
app.config.from_json(__instance_path)
app.url_map.strict_slashes = False

db.init_app(app)
base_schema.init_app(app)

app.register_blueprint(base_bp)
app.register_blueprint(user_bp)
app.register_blueprint(errors_bp)
db.create_all(app=app)
