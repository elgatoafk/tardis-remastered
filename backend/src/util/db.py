from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, sessionmaker

from backend.src.config import settings

DATABASE_URL = f"postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}/{settings.DB_NAME}"

Base = declarative_base()

engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True, pool_size=20, pool_recycle=3600)

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


def get_db():
    with SessionLocal() as session:
        try:
            yield session
        except OperationalError as e:
            session.rollback()
            raise e


def init_db():
    Base.metadata.create_all(bind=engine, checkfirst=True)
