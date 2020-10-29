from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Optional
from fastapi import Header

# SQLAlchemy specific code, as with any other app
driver = "postgresql"
host = "blah"
port = 5432
db = "postgres"
user = "postgres"
password = "blah" #dont do this
DATABASE_URL = f"postgresql://{user}:{password}@{host}/{db}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db(token: Optional[str] = Header(None)):
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()