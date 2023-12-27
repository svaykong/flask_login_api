from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

# create db object from SQLAlchemy
db = SQLAlchemy()

# create bcrypt object from Bcrypt
bcrypt = Bcrypt()

# create ma object from Marshmallow
ma = Marshmallow()
