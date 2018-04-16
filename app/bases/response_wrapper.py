# -*- coding: utf-8 -*-

from functools import wraps
from flask_api import status


class ResponseWrapper(object):

    @classmethod
    def resp(cls, func=None):
        @wraps(func)
        def wrapper(*args, **kw):
            response = func(*args, **kw)
            if not response:
                return cls.__no_content()
            if response:
                return cls.__ok(response)

        return wrapper

    @classmethod
    def __ok(cls, response):
        return response, status.HTTP_200_OK

    @classmethod
    def __no_content(cls):
        return '', status.HTTP_204_NO_CONTENT

    @classmethod
    def __created(cls):
        return '', status.HTTP_201_CREATED

    @classmethod
    def __message(cls, message):
        return message, 422
