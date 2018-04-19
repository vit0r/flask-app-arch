"""
cop-op marketing
"""

import os
from flask_api import FlaskAPI
from app.libraries import Library

__author__ = 'Vitor Nascimento de Araujo'

libbase = Library()

instance_name = libbase.__get__(__file__)

app = FlaskAPI(__name__, instance_path=instance_name, instance_relative_config=True)
app.config.from_json(instance_name)

libbase(app=app)


