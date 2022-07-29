from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine, orm
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import Config

engine = create_engine(Config.DATABASE_URL)

Base = declarative_base()

Session = sessionmaker(bind=engine)


def session_generator() -> Generator[orm.Session, None, None]:
    """Provide a transactional scope"""
    session = Session()
    try:
        yield session
        session.commit()
    except:  # noqaE722
        session.rollback()
        raise
    finally:
        session.close()


session_scope = contextmanager(session_generator)
