from pydantic import BaseModel
from typing import List


class Vuttr(BaseModel):
    id: int
    title: str
    link: str
    description: str

    class Config:
        from_attributes = True


class Tag(BaseModel):
    nome: str

    class Config:
        from_attributes = True


class TagList(BaseModel):
    tags: List[Tag]

    class Config:
        from_attributes = True


class VuttrList(BaseModel):
    tools: list[Vuttr]

    class Config:
        from_attributes = True
