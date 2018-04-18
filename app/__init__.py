"""
cop-op marketing
"""

import os
from flask_api import FlaskAPI
from app.bases import db, env, base_schema, register_blueprints

__author__ = 'Vitor Nascimento de Araujo'

__instance_path = os.path.join(os.path.dirname(__file__), 'instances', env + '.json')
app = FlaskAPI(__name__, instance_path=__instance_path, instance_relative_config=True)
app.config.from_json(__instance_path)
app.url_map.strict_slashes = False

db.init_app(app)
base_schema.init_app(app)

register_blueprints(app)

db.create_all(app=app)
