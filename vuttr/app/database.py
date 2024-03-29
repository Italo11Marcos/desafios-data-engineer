from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from settings import settings


engine = create_engine(url=settings.DB_URL, echo=False)


def get_session():
    with Session(engine) as session:
        yield session