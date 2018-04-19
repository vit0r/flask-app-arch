import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.utils import import_string

db = SQLAlchemy()
schema = Marshmallow()


class Library:
    def __call__(self, *args, **kwargs):
        self.app = kwargs.get('app')
        if self.app:
            self.app.url_map.strict_slashes = False
            self.__register_blueprints()
            db.init_app(self.app)
            schema.init_app(self.app)

    def __get__(self, *args, **kwargs):
        environ_name = os.environ.get('IS_HEROKU', 'develop')
        app_dir = os.path.dirname(*args)
        instance_file = os.path.join(app_dir, 'instances', environ_name + '.json')
        return instance_file

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, 'flask instance == app')

    def __register_blueprints(self):
        if self.app:
            bp_config = self.app.config['BLUEPRINTS']
            bp_dir = os.path.join(self.app.name, bp_config.get('path'))
            bp_files = filter(lambda f: f.endswith('_route.py'), os.listdir(bp_dir))
            for bp_file in bp_files:
                bp_name = os.path.basename(bp_file).replace('.py', '.bp')
                bp_mod = '.'.join([self.app.name, bp_config.get('path'), bp_name])
                bp_module_name = import_string(bp_mod)
                self.app.register_blueprint(bp_module_name, url_prefix=bp_config.get('prefix'))
