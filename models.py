"""Module defines SQLAlchemy models for the FastAPI app."""

from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class ToDo(Base):
    """Model for a to-do items."""

    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)  # unique ID
    title = Column(String, index=True)  # title of the to-do
    description = Column(String)  # description of the to-do
    completed = Column(Boolean, default=False)  # completion status
