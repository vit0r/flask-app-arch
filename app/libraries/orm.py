from app.libraries import db


class ORM(object):

    @classmethod
    def create(cls, data):
        try:
            db.session.add(data)
            db.session.commit()
        except ValueError as ex:
            db.session.rollback()
        finally:
            db.session.close()

    @classmethod
    def find(cls, model, data):
        result = model.query(data)
        return result

    @classmethod
    def find_all(cls, model):
        results = model.query.all()
        return results
