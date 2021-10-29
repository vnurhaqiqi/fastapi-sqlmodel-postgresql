from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlmodel import Session

from db import init_db, get_session
from models import *

app = FastAPI()


# @app.on_event("startup")
# def on_startup():
#     init_db()


@app.get("/")
async def index():
    return {"Hello": "World"}


@app.get("/films", response_model=List[Film])
def get_films(*, session: Session = Depends(get_session)):
    films = session.exec(select(Film)).scalars().all()

    return films


@app.post("/films", response_model=Film)
def create_film(*, session: Session = Depends(get_session), film: FilmCreate):
    add_film = Film.from_orm(film)
    session.add(add_film)
    session.commit()
    session.refresh(add_film)

    return add_film


@app.get("/films/{film_id}", response_model=Film)
def get_film_by_id(*, session: Session = Depends(get_session), film_id: int):
    film = session.get(Film, film_id)

    if not film:
        raise HTTPException(status_code=404, detail="Film not found.")

    return film


@app.delete("/films/{film_id}")
def delete_film_by_id(*, session: Session = Depends(get_session), film_id: int):
    film = session.get(Film, film_id)

    if not film:
        raise HTTPException(status_code=404, detail="Film not found.")

    session.delete(film)
    session.commit()

    return {"Success"}


@app.patch("/films/{film_id}", response_model=Film)
def update_film_by_id(*, session: Session = Depends(get_session), film_id: int, film: FilmUpdate):
    film_obj = session.get(Film, film_id)

    if not film_obj:
        raise HTTPException(status_code=404, detail="Film not found.")

    film_data = film.dict(exclude_unset=True)
    for key, value in film_data.items():
        setattr(film_obj, key, value)

    session.add(film_obj)
    session.commit()
    session.refresh(film_obj)

    return film_obj


@app.get("/genres", response_model=List[Genre])
def get_genres(*, session: Session = Depends(get_session)):
    genres = session.exec(select(Genre)).scalars().all()

    return genres


@app.post("/genres", response_model=Genre)
def create_genre(*, session: Session = Depends(get_session), genre: GenreCreate):
    add_genre = Genre.from_orm(genre)

    session.add(add_genre)
    session.commit()
    session.refresh(add_genre)

    return add_genre


@app.get("/genres/{genre_id}", response_model=Genre)
def get_genre_by_id(*, session: Session = Depends(get_session), genre_id: int):
    genre = session.get(Genre, genre_id)

    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found.")

    return genre


@app.delete("/genres/{genre_id}")
def delete_genre_by_id(*, session: Session = Depends(get_session), genre_id: int):
    genre = session.get(Genre, genre_id)

    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found.")

    session.delete(genre)
    session.commit()

    return {"Success"}


@app.patch("/genres/{genre_id}", response_model=Genre)
def update_genre_by_id(*, session: Session = Depends(get_session), genre_id: int, genre: GenreUpdate):
    genre_obj = session.get(Genre, genre_id)

    if not genre_obj:
        raise HTTPException(status_code=404, detail="Genre not found.")

    genre_data = genre.dict(exclude_unset=True)
    for key, value in genre_data.items():
        setattr(genre_obj, key, value)

    session.add(genre_obj)
    session.commit()
    session.refresh(genre_obj)

    return genre_obj
