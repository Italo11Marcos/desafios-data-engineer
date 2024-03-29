from sqlalchemy import ForeignKey, Column, String, Integer, Table
from sqlalchemy.orm import DeclarativeBase, relationship
from pydantic import BaseModel


class Base(DeclarativeBase):
    pass


vuttr_tag_association = Table(
    'vuttr_tag',
    Base.metadata,
    Column('vuttr_id', Integer, ForeignKey('vuttrs.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)


class VuttrModel(Base):
    __tablename__: str = 'vuttrs'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String)
    link: str = Column(String)
    description: str = Column(String)

    # Relacionamento Many-to-Many com a tabela Tag
    tags = relationship("TagModel", secondary=vuttr_tag_association, back_populates="vuttrs")

    def __repr__(self) -> str:
        return f'{self.title}'
    

class TagModel(Base):
    __tablename__: str = 'tags'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String)

    # Relacionamento Many-to-Many com a tabela Vuttr
    vuttrs = relationship("VuttrModel", secondary=vuttr_tag_association, back_populates="tags")

    def __repr__(self) -> str:
        return f'{self.nome}'
    

