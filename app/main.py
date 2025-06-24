from fastapi import FastAPI
from app.routes import dream

app = FastAPI(title="Dreamscope API")

app.include_router(dream.router)