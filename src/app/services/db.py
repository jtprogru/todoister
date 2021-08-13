from app.core import Base, SessionLocal, engine


async def create_database():
    return Base.metadata.create_all(bind=engine)


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
