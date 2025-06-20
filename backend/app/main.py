from fastapi import FastAPI
from backend.app.api import routes

app = FastAPI()

app.include_router(routes.router)
