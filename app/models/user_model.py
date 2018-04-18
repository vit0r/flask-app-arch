from app.bases import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    app_name = db.Column(db.String, nullable=False)
    user_name = db.Column(db.String, unique=True, nullable=False)
