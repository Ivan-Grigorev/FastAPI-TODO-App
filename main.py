"""Main entry point for the FastAPI app, defining API routes and handlers."""

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import SessionLocal, engine

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency to get a database session
def get_db():
    """Create a new database session for each request."""

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create a new to-do item
@app.post('/todos/', response_model=schemas.ToDoResponse)
def create_todo(todo: schemas.ToDoCreate, db: Session = Depends(get_db)):
    """Endpoint to create a new to-do."""

    db_todo = models.ToDo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


# Get all to-do items
@app.get('/todos/', response_model=List[schemas.ToDoResponse])
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Endpoint to retrieve all to-do items."""

    todos = db.query(models.ToDo).offset(skip).limit(limit=limit).all()
    return todos


# Get a single to-do item by ID
@app.get('/todos/{todo_id}', response_model=schemas.ToDoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    """Endpoint to retrieve a to-do by ID."""

    todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail='ToDo does not exist')
    return todo


# Update an existing to-do item
@app.put('/todos/{todo_id}', response_model=schemas.ToDoResponse)
def update_todo(todo_id: int, todo: schemas.ToDoUpdate, db: Session = Depends(get_db)):
    """Endpoint to update a to-do by ID."""

    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail='ToDo does not exist')

    for key, value in todo.dict().items():
        setattr(db_todo, key, value)

    db.commit()
    db.refresh(db_todo)
    return db_todo


# Delete a to-do item
@app.delete('/todos/{todo_id}')
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Endpoint to delete a to-do by ID"""

    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail='ToDo does not exist')

    db.delete(db_todo)
    db.commit()
    return {'message': 'ToDo deleted'}
