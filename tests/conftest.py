import pytest
from sqlalchemy_utils import create_database, database_exists, drop_database


@pytest.fixture(scope="package")
def db_setup():
    from app.config import Config

    # Clear the database and recreate it
    database_url = Config.DATABASE_URL + "/test"
    if database_exists(database_url):
        drop_database(database_url)
    create_database(database_url)


@pytest.fixture
def table_setup(db_setup):
    from app.db.base import Base, engine

    breakpoint()
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)
