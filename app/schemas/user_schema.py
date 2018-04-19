from flask_marshmallow.sqla import ModelSchema
from marshmallow import post_load
from app.libraries.orm import ORM
from app.models.user_model import UserModel


class UserSchema(ModelSchema):
    class Meta:
        model = UserModel

    @post_load
    def __parse(self, user):
        return UserModel(**user)

    def find(self, user):
        user = ORM.find(UserModel, user)
        data = super().dump(obj=user)
        return data

    def find_all(self):
        users = ORM.find_all(UserModel)
        data = super().dump(users, many=True)
        return data

    def create(self, user):
        user_data = self.__parse(user)
        ORM.create(user_data)
