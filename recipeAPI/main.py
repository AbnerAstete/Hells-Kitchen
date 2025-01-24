from fastapi import FastAPI
from router import recipe

app = FastAPI()
app.include_router(recipe.recipe_router)

