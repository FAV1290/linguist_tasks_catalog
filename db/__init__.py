import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker


from webapp.config import DB_HOST


class Base(sqlalchemy.orm.DeclarativeBase):
    engine = sqlalchemy.create_engine(DB_HOST, pool_size=10)
    db_session = scoped_session(sessionmaker(bind=engine))
    query = db_session.query_property()
