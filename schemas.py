"""Module defines Pydantic models for data validation in the FastAPI app."""

from pydantic import BaseModel


class ToDoBase(BaseModel):
    """Base model for a to-do item."""

    title: str  # title of the to-do
    description: str  # description of the to-do
    completed: bool = False  # completion status


class ToDoCreate(ToDoBase):
    """Model for creating a new to-do item."""

    pass


class ToDoUpdate(ToDoBase):
    """Model for updating an existing to-do item"""

    pass


class ToDoResponse(ToDoBase):
    """Model for the response of a to-do item."""

    id: int  # unique ID of the to-do

    class Config:
        from_attributes = True  # enable ORM mode for data conversion
