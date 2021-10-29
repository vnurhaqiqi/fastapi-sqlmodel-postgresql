from fastapi import FastAPI, Depends
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
