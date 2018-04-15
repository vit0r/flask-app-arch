"""
cop-op marketing
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api
from os import path
from api.routes import base_bp
from api.bases import BaseUtils

__author__ = 'Vitor Nascimento de Araujo'

instance_path = path.join(path.dirname(__file__), 'instances', BaseUtils.instance_file())
app = Flask(__name__, instance_path=instance_path, instance_relative_config=True)
app.config.from_json(instance_path)
app.url_map.strict_slashes = False
db = SQLAlchemy(app)
api = Api(base_bp, doc='/docs')
app.register_blueprint(base_bp)
