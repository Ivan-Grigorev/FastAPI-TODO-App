"""Module sets up the database connection for the FastAPI app using SQLAlchemy."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL for SQLite
DATABASE_URL = 'sqlite:///./fastapi_todo_app.db'

# Create the database engine
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

# SessionLocal to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for SQLAlchemy models
Base = declarative_base()
