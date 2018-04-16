from app.bases import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    app_name = db.Column(db.String)
    user_name = db.Column(db.String)
