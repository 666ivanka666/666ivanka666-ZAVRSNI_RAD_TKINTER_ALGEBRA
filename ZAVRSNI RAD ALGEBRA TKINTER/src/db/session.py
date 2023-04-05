from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()


def create_session():
    db_name = "PyPosuda.db"
    db_engine = create_engine(f"sqlite:///db/{db_name}")

    return Session(db_engine)

def init():
    db_name = "PyPosuda.db"
    db_engine = create_engine(f"sqlite:///db/{db_name}")
    Base.metadata.drop_all(db_engine)
    Base.metadata.create_all(db_engine)

    return Session(db_engine)
