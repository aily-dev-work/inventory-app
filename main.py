from fastapi import FastAPI
from app.routers import router

app = FastAPI(title="Inventory App")

app.include_router(router)

@app.get("/")
def health():
    return {"status": "ok"}