"""
cop-op marketing
"""

from flask import Flask
from flask_restplus import Api
from os import path
from api.routes import swagger_bp

__author__ = 'Vitor Nascimento de Araujo'

instance_path = path.join(path.dirname(__file__), 'instances', 'master.json')
app = Flask(__name__, instance_path=instance_path, instance_relative_config=True)
app.config.from_json(instance_path)
app.url_map.strict_slashes = False
api = Api(swagger_bp)
app.register_blueprint(swagger_bp)
