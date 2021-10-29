from sqlmodel import SQLModel, Field
from typing import Optional, List


class FilmBase(SQLModel):
    name: str
    released_year: int
    director: str


class Film(FilmBase, table=True):
    id: int = Field(default=None, primary_key=True)


class FilmCreate(FilmBase):
    pass
