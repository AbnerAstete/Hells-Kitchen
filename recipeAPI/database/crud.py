from sqlalchemy.orm import Session

from model import model
from model.model import Recipe

from schemas import schemas

from  datetime import datetime


def create(recipe: schemas.Recipe, db: Session):
    current_date_time = datetime.now()
    recipe = Recipe(title=recipe.title,
                    ingredients=recipe.ingredients,
                    disabled = False, 
                    directions=recipe.directions,
                    ner = recipe.ner,
                    created_at=current_date_time)
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe

def edit(id:int,data: schemas.RecipeUpdate, db: Session):
    update_data = data.dict(exclude_unset=True)
    db.query(Recipe).filter(Recipe.id == id).update(update_data)
    db.commit()
    updated_recipe = find_by_id(db, id)
    return updated_recipe

def delete(id:int, db: Session):
    recipe = db.query(Recipe).filter(Recipe.id == id).first()
    db.delete(recipe)
    db.commit()
    
def find_by_title(db: Session, title:str):
    return db.query(Recipe).filter(Recipe.title==title).first()

def find_by_id(db: Session, id:int):
    return db.query(Recipe).filter(Recipe.id==id).first()