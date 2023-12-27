from flask_sqlalchemy import SQLAlchemy


def init_db(app=None) -> SQLAlchemy:
    db = SQLAlchemy(app)
    return db
