from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic

from sqlalchemy.orm import Session

from database import crud
from database.database import engine, get_db

from model import model

from schemas import schemas



recipe_router = APIRouter()
security = HTTPBasic()
model.Base.metadata.create_all(bind=engine)

@recipe_router.post("/recipes/create")
def create_recipe(recipe: schemas.Recipe, db: Session = Depends(get_db)):
    title = crud.find_by_title(db,title=recipe.title)
    if title:
        raise HTTPException(status_code=400, detail="Recipe already registered")
    return crud.create(recipe, db)

@recipe_router.get("/recipes/{recipe_id}")
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = crud.find_by_id(db, recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@recipe_router.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    existing_recipe = crud.find_by_id(db, recipe_id)
    if existing_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    updated_recipe = crud.edit(recipe_id,recipe,db)
    return updated_recipe

@recipe_router.delete("/recipes/{recipe_id}")
async def delete_item(recipe_id: int, db: Session = Depends(get_db)):
    recipe = crud.find_by_id(db, recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    
    try:
        crud.delete(recipe_id,db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return {"detail": "Recipe deleted successfully"}