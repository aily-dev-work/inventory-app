from fastapi import FastAPI

from app.db import Base, engine
from app.routers import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
