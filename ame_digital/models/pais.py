from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Float
from models.model_base import Base

from datetime import datetime


class Pais(Base):
    __tablename__: str = 'paises'

    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    nome: str = Column(String(100))

    def __repr__(self) -> str:
        return f'{self.nome}'
