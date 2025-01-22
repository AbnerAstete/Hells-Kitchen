from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic


from sqlalchemy.orm import Session

from database.database import engine, get_db
from database import crud
from model import model
from schemas import schemas

import httpx
import os


item_router = APIRouter()
security = HTTPBasic()
model.Base.metadata.create_all(bind=engine)


@item_router.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@item_router.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@item_router.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items