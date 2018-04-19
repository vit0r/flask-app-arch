from app import app

__author__ = 'Vitor Nascimento de Araujo'

if __name__ == '__main__':
    debug = app.config.get('DEBUG')
    app.run(debug=debug)
