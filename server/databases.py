from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:ramprk97@localhost:5432/studentsreport"
SQLALCHEMY_DATABASE_URL = "postgresql://studentsreport_user:ZRWFo9GJigh3qZNDsMVG8eQmZWxufeR6@dpg-crt7mi3tq21c73dljprg-a.oregon-postgres.render.com/studentsreport"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
