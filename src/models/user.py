from ..app import db, bcrypt


class User(db.Model):
    """docstring for User"""
    __tablename__ = "users"
    id = db.Column(db.Integer, db.Sequence("user_id_seq"), primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True)

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
