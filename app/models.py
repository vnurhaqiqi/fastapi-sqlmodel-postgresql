from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class FilmBase(SQLModel):
    name: str
    released_year: int
    director: str

    genre_id: Optional[int] = Field(default=None, foreign_key="genre.id")


class Film(FilmBase, table=True):
    id: int = Field(default=None, primary_key=True)

    genre: Optional["Genre"] = Relationship(back_populates="films")


class FilmCreate(FilmBase):
    pass


class FilmUpdate(SQLModel):
    name: Optional[str] = None
    released_year: Optional[int] = None
    director: Optional[str] = None
    genre_id: Optional[int] = None


class GenreBase(SQLModel):
    name: str


class Genre(GenreBase, table=True):
    id: int = Field(default=None, primary_key=True)

    films: List[Film] = Relationship(back_populates="genre")


class GenreCreate(GenreBase):
    pass


class GenreUpdate(SQLModel):
    name: Optional[str]
