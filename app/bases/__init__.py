from os import environ
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

env = environ.get('IS_HEROKU', 'develop')
db = SQLAlchemy()
base_schema = Marshmallow()
