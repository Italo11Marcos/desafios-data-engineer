from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Float
from models.model_base import Base

from datetime import datetime


class SistemaOperacional(Base):
    __tablename__: str = 'sistemas_operacionais'

    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    nome: str = Column(String(100))

    def __repr__(self) -> str:
        return f'{self.nome}'