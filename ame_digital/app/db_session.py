import os

import sqlalchemy as sa

from sqlalchemy.orm import sessionmaker, Session

from pathlib import Path # Usado no SQLite
from typing import Optional

from sqlalchemy.future.engine import Engine

from models.model_base import Base

__engine: Optional[Engine] = None

DB=os.getenv('POSTGRES_DB')
USER=os.getenv('POSTGRES_USER')
PASSWORD=os.getenv('POSTGRES_PASSWORD')
HOST=os.getenv('POSTGRES_HOST')
PORT=os.getenv('POSTGRES_PORT')


def create_engine(sqlite: bool = False) -> Engine:
    """
    Função para configurar a conexão ao banco de dados.
    """
    global __engine

    if __engine:
        return
    """
    if sqlite:
        arquivo_db = 'db/produto.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)

        conn_str = f'sqlite:///{arquivo_db}'
        __engine = sa.create_engine(url=conn_str, echo=True, connect_args={"check_same_thread": False})
    
    else:
        conn_str = "postgresql://user:password@localhost:5432/database"
        __engine = sa.create_engine(url=conn_str, echo=False)
    """
    conn_str = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine


def create_session() -> Session:
    """
    Função para criar sessão de conexao ao banco de dados.
    """
    global __engine

    if not __engine:
        create_engine() # create_engine(sqlite=True)
    
    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session: Session = __session()

    return session


def create_tables() -> None:
    global __engine

    if not __engine:
        create_engine(sqlite=True)
    
    import models.__all_models
    Base.metadata.drop_all(__engine)
    Base.metadata.create_all(__engine)