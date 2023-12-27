"""
import bcrypt
from sqlalchemy import Sequence, Column, Integer, String

from src.database import Base
"""

"""
To define your models, just subclass the Base class that was created by the code above. 
If you are wondering why we don’t have to care about threads here (like we did in the SQLite3 example above with the g object): 
that’s because SQLAlchemy does that for us already with the scoped_session.
"""

# class User(Base):
"""docstring for User"""

"""
__tablename__ = "users"
id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
username = Column(String(50), unique=True, nullable=False)
password_hash = Column(String(255), nullable=False)
email = Column(String(120), unique=True)

def __init__(self, username=None, email=None, pwd=None):
    self.username = username

    # hash password start
    self.password = pwd
    # self.__make_password(pwd)

    self.email = email

@property
def password(self):
    raise AttributeError('password not readable')

@password.setter
def password(self, password):
    enc_pw = password.encode('utf-8')
    self.password_hash = bcrypt.hashpw(enc_pw, bcrypt.gensalt()).decode('utf-8')

def __make_password(self, password):
    enc_pw = password.encode('utf-8')
    self.password_hash = bcrypt.hashpw(enc_pw, bcrypt.gensalt()).decode('utf-8')

def verify_password(self, password):
    enc_pw = password.encode('utf-8')
    return bcrypt.checkpw(enc_pw, bytes(self.password_hash, 'utf-8'))

def __repr__(self):
    return f'<User(username={self.username}, email={self.email})>'
"""
