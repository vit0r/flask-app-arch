class BaseUtils(object):

    @staticmethod
    def instance_file():
        from os import environ
        is_heroku = environ.get('IS_HEROKU', None)
        if is_heroku:
            return 'master.json'
        return 'develop.json'
