import httpx
import os

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from database import crud
from database.database import engine, get_db

from model import model

from schemas import schemas

from typing import Annotated

from utils.utils import get_current_user, authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

from datetime import timedelta

user_router = APIRouter()
security = HTTPBasic()
model.Base.metadata.create_all(bind=engine)

@user_router.post("/users/create")
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    username = crud.find_by_username(db,username=user.username)
    email = crud.find_by_email(db,email=user.email)
    if email:
        raise HTTPException(status_code=400, detail="Email already registered")
    elif username:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create(user, db)


@user_router.get("/users/me")
async def read_users_me(current_user: Annotated[schemas.User, Depends(get_current_user)]):
    return current_user

@user_router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db),
) -> schemas.Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return schemas.Token(access_token=access_token, token_type="bearer")