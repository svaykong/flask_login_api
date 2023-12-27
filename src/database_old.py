from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

""" Example of using psycopg2 """
"""
import psycopg2

# connect to postgresql database
conn = psycopg2.connect(host='localhost', dbname='testdb', user='postgres', password='admin', port=5432)
"""

""" Example of using SQLAlchemy """
"""
import sqlalchemy as db

engine = db.create_engine("postgresql+psycopg2://postgres:admin@localhost:5432/testdb")
conn = engine.connect()
"""

""" Example of using Flask-SQLAlchemy """

# create engine object
# set logging (echo=True) to display log
engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/testdb', echo=True)

# create db session object
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

# create Base object
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    """
    import yourapplication.models
    Base.metadata.create_all(bind=engine)
    """

    return db_session
