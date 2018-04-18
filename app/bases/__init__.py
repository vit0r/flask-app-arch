import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.utils import import_string

env = os.environ.get('IS_HEROKU', 'develop')
db = SQLAlchemy()
base_schema = Marshmallow()


def register_blueprints(app):
    bp_config = app.config['BLUEPRINTS']
    bp_dir = os.path.join(app.name, bp_config.get('path'))
    bp_files = filter(lambda f: f.endswith('_route.py'), os.listdir(bp_dir))
    for bp_file in bp_files:
        bp_name = os.path.basename(bp_file).replace('.py', '.bp')
        bp_mod = '.'.join([app.name, bp_config.get('path'), bp_name])
        bp_module_name = import_string(bp_mod)
        app.register_blueprint(bp_module_name, url_prefix=bp_config.get('prefix'))
