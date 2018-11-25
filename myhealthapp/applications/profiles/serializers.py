from config import marshmallow
from .models import User

__all__ = ['UserSerializer', 'UsersSerializer']


class UserSchema(marshmallow.ModelSchema):

    class Meta:
        model = User


UserSerializer = UserSchema()
UsersSerializer = UserSchema(many=True)
