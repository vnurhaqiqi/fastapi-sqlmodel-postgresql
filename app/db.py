import os

from sqlmodel import create_engine, SQLModel, Session

# DATABASE_URL = os.environ.get("")
DATABASE_URL = "YOUR-DATABASE-NAME"
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
