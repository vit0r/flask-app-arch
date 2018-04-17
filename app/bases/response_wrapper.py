# -*- coding: utf-8 -*-

from functools import wraps
from flask import request
from flask_api import status


class ResponseWrapper(object):

    @classmethod
    def resp(cls, func=None):
        @wraps(func)
        def wrapper(*args, **kw):
            resp = func(*args, **kw)
            if request.method == 'POST':
                return cls.__created()
            if not resp:
                return cls.__no_content()
            if resp:
                return cls.__ok(resp)

        return wrapper

    @classmethod
    def __ok(cls, resp):
        return {'data': resp}, status.HTTP_200_OK

    @classmethod
    def __no_content(cls):
        return '', status.HTTP_204_NO_CONTENT

    @classmethod
    def __created(cls):
        return '', status.HTTP_201_CREATED
