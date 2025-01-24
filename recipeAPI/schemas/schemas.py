from pydantic import BaseModel
from typing import List, Optional

class Recipe(BaseModel):
    title: str
    ingredients: List[str] 
    directions: List[str] 
    ner: List[str] 

class RecipeUpdate(BaseModel):
    title: Optional[str] = None
    ingredients: Optional[List[str]] = None
    directions: Optional[List[str]] = None
    ner: Optional[List[str]] = None