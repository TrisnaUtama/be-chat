from sqlmodel import Session, create_engine

from app.core.settings import settings

engine = create_engine(settings.DATABASE_URL, echo=True, connect_args={})

def get_session():
    with Session(engine) as session:
        yield session
