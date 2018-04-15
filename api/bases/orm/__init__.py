from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from api.models import *


class ORM(object):

    def __init__(self, uri_database):
        self.__engine = create_engine(uri_database, convert_unicode=True)
        self.__db_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=self.__engine))
        self.__base = declarative_base()
        self.__base.query = self.__db_session.query_property()

    def create_db(self):
        self.__base.metadata.create_all(bind=self.__engine)

    @property
    def db_session(self):
        return self.__db_session
