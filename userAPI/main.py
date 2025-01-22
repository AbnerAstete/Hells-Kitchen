from fastapi import FastAPI
from userAPI.router import item

app = FastAPI()
app.include_router(item.item_router)