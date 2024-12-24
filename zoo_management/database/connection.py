from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mssql+pyodbc://DESKTOP-L8A1O1P\\SQLEXPRESS/Zoo_db?driver=SQL+Server+Native+Client+11.0&trusted_connection=yes"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()