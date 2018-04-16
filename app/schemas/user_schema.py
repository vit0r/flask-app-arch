from marshmallow import post_load
from app.bases import base_schema
from app.models.user_model import UserModel


class UserSchema(base_schema.ModelSchema):
    class Meta:
        model = UserModel

    @post_load
    def parse(self, user):
        return UserModel(**user)

    def find(self,user):
        user = UserModel.query(self.__user)
        data = super().dump(obj=user)
        return data

    def find_all(self):
        users = UserModel.query.all()
        data = super().dump(users, many=True)
        return data
