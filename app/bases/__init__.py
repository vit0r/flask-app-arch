from os import environ
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

env = 'master' if environ.get('IS_HEROKU', None) else 'develop'
db = SQLAlchemy()
base_schema = Marshmallow()
