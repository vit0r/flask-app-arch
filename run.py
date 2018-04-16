"""
cop-op marketing
"""

from app import app

__author__ = 'Vitor Nascimento de Araujo'

if __name__ == '__main__':
    has_debug = app.config.get('DEBUG')
    app.run(debug=has_debug)
