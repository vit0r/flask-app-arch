from app.schemas.user_schema import UserSchema


class UserModule(UserSchema):

    def find(self, user):
        return super().find(user)

    def find_all(self):
        users = super().find_all()
        return users

    def create(self, user):
        super().create(user)
