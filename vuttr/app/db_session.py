import os
import sqlalchemy

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine
from typing import Optional

from models import Base


__engine: Optional[Engine] = None


DB=os.getenv('POSTGRES_DB')
USER=os.getenv('POSTGRES_USER')
PASSWORD=os.getenv('POSTGRES_PASSWORD')
HOST=os.getenv('POSTGRES_HOST')
PORT=os.getenv('POSTGRES_PORT')


def create_engine() -> Engine:
    """
    Função para configurar a conexão com o banco de dados
    """
    global __engine

    if __engine:
        return

    conn_str = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    __engine = sqlalchemy.create_engine(url=conn_str, echo=False)

    return __engine


def create_session() -> Session:
    """
    Função para criar a sessão de conexão com o banco de dados
    """
    global __engine

    if not __engine:
        create_engine()

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session: Session = __session()

    return session


def create_tables() -> None:
    global __engine

    if not __engine:
        create_engine()

    Base.metadata.drop_all(__engine)
    Base.metadata.create_all(__engine)