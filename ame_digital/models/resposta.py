from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Float
from models.model_base import Base

from datetime import datetime


class Resposta(Base):
    __tablename__: str = 'respostas'

    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    respondent: int = Column(BigInteger)
    hobby: str = Column(String(3))
    opensource: str = Column(String(3))
    country: str = Column(String(45))
    companysize: str = Column(String(100))
    communicationtools: str = Column(String(100))
    languageworked: str = Column(String(100))
    salary: float = Column(Float)
    operatingsystem: str = Column(String(35))
    language_rank: float = Column(Float)
    communication_rank: float = Column(Float)

    def __repr__(self) -> str:
        return f'{self.respondent}_{self.id}>'