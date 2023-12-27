from src.app import ma
from src.models.user import User


# Create a Marshmallow schema for the User model
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
