import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture
def db_session():
    """In-memory SQLite for unit tests. Never hits production DB."""
    engine = create_engine("sqlite:///:memory:")
    # TODO: Import Base from entities and create tables
    # from src.entities.base import Base
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
