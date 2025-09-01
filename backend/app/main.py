from fastapi import FastAPI
from app.api import melodies

app = FastAPI()
app.include_router(melodies.router, prefix="/melodies")
