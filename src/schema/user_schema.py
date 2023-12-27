from ..helper import ma
from ..models.user import User


# Create a Marshmallow schema for the User model
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
