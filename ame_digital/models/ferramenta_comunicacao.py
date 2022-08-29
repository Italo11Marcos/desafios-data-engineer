from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Float
from models.model_base import Base

from datetime import datetime

from sqlalchemy.orm import relationship

class FerramentaComunicacao(Base):
    __tablename__: str = 'ferramentas_comunicacao'

    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    respondentes = relationship('Respondente', secondary = 'resp_usa_ferramenta', cascade="all, delete")


    def __repr__(self) -> str:
        return f'{self.nome}'