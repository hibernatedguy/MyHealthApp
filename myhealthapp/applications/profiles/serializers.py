from config import marshmallow
from .models import User

__all__ = ['UserSerializer', 'UsersSerializer']


class UserSchema(marshmallow.ModelSchema):

    class Meta:
        model = User


UserSerializer = UserSchema(exclude=['password'])
UsersSerializer = UserSchema(exclude=['password'], many=True)
