from config import marshmallow
from .models import Checkup

__all__ = ['CheckupSerializer', 'CheckupsSerializer']


class CheckupSchema(marshmallow.ModelSchema):

    class Meta:
        model = Checkup


CheckupSerializer = CheckupSchema()
CheckupsSerializer = CheckupSchema(many=True)
