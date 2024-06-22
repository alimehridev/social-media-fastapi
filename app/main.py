# General imports
from fastapi import FastAPI
# Database imports
from . import models
from .database import engine
from app.routers import post, user

models.Base.metadata.create_all(bind=engine)
app = FastAPI() 

# Including routers
app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
async def root():
    return {"message": "Welcome to my api"}