import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from src.routes.auth import auth

# load dotenv file (.env)
load_dotenv(dotenv_path='../.env')

# define constants variables
BASE_URL = os.environ.get('BASE_URL')
PORT = os.environ.get('PORT')
HOST = os.environ.get('HOST')
DEBUG = os.environ.get('DEBUG')

# create the app object from Flask
app = Flask(__name__)

# register auth route
app.register_blueprint(auth, url_prefix=BASE_URL + '/auth')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@localhost:5432/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize SQLAlchemy database object (db)
db = SQLAlchemy(app)

# create ma of marshmallow object
ma = Marshmallow(app)

# create the bcrypt object from Bcrypt
bcrypt = Bcrypt(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(port=PORT, host=HOST, debug=DEBUG)
