from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
"""
while True:
    try:
        # bad practice, will be improved later
        conn = psycopg2.connect(host='localhost', database='fastapi', 
                            user='postgres', password='123456',
                            cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful!")
        break

    except Exception as error:
        print("Connection to database is failed")
        print("Error:", error)
        time.sleep(2)
"""