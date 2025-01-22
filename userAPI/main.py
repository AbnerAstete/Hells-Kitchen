from fastapi import FastAPI
from router import item

app = FastAPI()
app.include_router(item.item_router)