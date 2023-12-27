import os

from dotenv import load_dotenv
from flask import Flask
from src.helper import db, bcrypt, ma
from src.routes.auth import auth

load_dotenv(dotenv_path='.env')  # load dotenv file (.env)

# define constants variables
BASE_URL = os.environ.get('BASE_URL')
PORT = os.environ.get('PORT')
HOST = os.environ.get('HOST')
DEBUG = os.environ.get('DEBUG')
DATABASE_URI = os.environ.get('DATABASE_URI')

app = Flask(__name__)  # create the app object from Flask

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# register all routes
app.register_blueprint(auth, url_prefix=BASE_URL + '/auth')

db.init_app(app)  # initialize SQLAlchemy
bcrypt.init_app(app)  # initialize Bcrypt
ma.init_app(app)  # initialize Marshmallow

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(port=PORT, host=HOST, debug=DEBUG)
