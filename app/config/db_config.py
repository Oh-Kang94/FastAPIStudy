import os

from sqlmodel import Session, SQLModel, create_engine

db_user = os.getenv("DB_USER")
db_pw = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
engine = create_engine(
    f"mysql+pymysql://{db_user}:{db_pw}@localhost:3306/{db_name}", echo=True
)


def conn():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
