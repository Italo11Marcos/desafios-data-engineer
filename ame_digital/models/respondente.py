from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Float, ForeignKey, Table

from models.ferramenta_comunicacao import FerramentaComunicacao
from models.linguagem_programacao import LinguagemProgramacao
from models.sistema_operacional import SistemaOperacional

from models.model_base import Base

from typing import List, Optional

from sqlalchemy.orm import relationship

class Respondente(Base):
    __tablename__: str = 'respondente'

    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    contrib_open_source: int = Column(Integer)
    programa_hobby: int = Column(Integer)
    salario: float = Column(Float)
    sistema_operacional_id: int = Column(Integer, ForeignKey("sistemas_operacionais.id",ondelete="CASCADE"))
    pais_id: int = Column(Integer, ForeignKey('paises.id',ondelete="CASCADE"))
    empresa_id: int = Column(Integer, ForeignKey('empresas.id',ondelete="CASCADE"))


    def __repr__(self) -> str:
        return f'{self.nome}'


class RespUsaFerramenta(Base):
   __tablename__ = 'resp_usa_ferramenta'
   id: int = Column(BigInteger, primary_key=True, autoincrement=True)
   ferramenta_comunic_id = Column(Integer, ForeignKey('ferramentas_comunicacao.id',ondelete="CASCADE"))
   respondente_id = Column(Integer, ForeignKey('respondente.id'))

class RespUsaLinguagem(Base):
   __tablename__ = 'resp_usa_linguagem'
   id: int = Column(BigInteger, primary_key=True, autoincrement=True)
   linguagem_programacao_id = Column(Integer, ForeignKey('linguagens_programacao.id',ondelete="CASCADE"))
   respondente_id = Column(Integer, ForeignKey('respondente.id'))