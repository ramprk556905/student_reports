import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection parameters
DB_HOST = "dpg-crt7mi3tq21c73dljprg-a.oregon-postgres.render.com"
DB_USER = "studentsreport_user"
DB_PASSWORD = "ZRWFo9GJigh3qZNDsMVG8eQmZWxufeR6"
DB_NAME = "studentsreport"
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}"

# Function to check if the database exists and create it if it doesn't
def create_database_if_not_exists(db_name):
    try:
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(
            dbname='postgres',  # Connect to the default 'postgres' database
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Check if the database exists
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'")
        exists = cursor.fetchone()
        
        if not exists:
            # Create the database if it doesn't exist
            cursor.execute(f"CREATE DATABASE {db_name}")
            print(f"Database '{db_name}' created successfully.")
        else:
            print(f"Database '{db_name}' already exists.")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error creating database: {e}")

# Call the function to create the database if not exist
create_database_if_not_exists(DB_NAME)

# SQLAlchemy setup
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Function to create the database tables if they don't exist
def create_tables():
    # Import your models here to ensure they are registered with Base
    import models  # Replace with your actual models module
    Base.metadata.create_all(bind=engine)

# Call the function to create tables if not exist
if __name__ == "__main__":
    create_tables()
