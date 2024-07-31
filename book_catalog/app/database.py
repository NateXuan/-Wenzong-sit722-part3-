from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://wenzong_sit722_user:opJoTHqOzqQK2kjaYKiDKGpaorF1VEpf@dpg-cqg9kdtds78s73catas0-a.oregon-postgres.render.com/wenzong_sit722" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
