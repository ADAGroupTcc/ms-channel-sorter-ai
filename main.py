from fastapi import FastAPI
from app.routes import router
from app.input import insert_random_users

app = FastAPI()
app.include_router(router)
# insert_random_users()