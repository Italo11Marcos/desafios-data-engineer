from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Float
from models.model_base import Base

from datetime import datetime


class Empresa(Base):
    __tablename__: str = 'empresas'

    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    tamanho: str = Column(String(100))

    def __repr__(self) -> str:
        return f'{self.tamanho}_{self.id}>'
