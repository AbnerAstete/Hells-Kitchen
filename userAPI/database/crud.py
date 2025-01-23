from sqlalchemy.orm import Session

from model import model
from model.model import User

from schemas import schemas

from utils.utils import pwd_context

from  datetime import datetime


def create(user: schemas.User, db: Session):
    current_date_time = datetime.now()
    hashed_password = pwd_context.hash(user.hashed_password) 
    user = User(    username=user.username,
                    email=user.email,
                    created_at=current_date_time,
                    disabled = False, 
                    hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def find_by_email(db: Session, email:str):
    return db.query(User).filter(User.email==email).first()

def find_by_username(db: Session, username:str):
    return db.query(User).filter(User.username==username).first()