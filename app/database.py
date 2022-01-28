from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import psycopg2
from psycopg2.extras import RealDictCursor 
import time

from .config import settings

print(settings.database_hostname)
#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Tigger%40313@localhost/fastapi'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'

engine = create_engine( SQLALCHEMY_DATABASE_URL )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Tigger@313', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database Connected Successfully.....")
#         break
#     except Exception as error:
#         print("Connection to Database Failed !!!!")
#         print("Error: ", error)    
#         time.sleep(2)