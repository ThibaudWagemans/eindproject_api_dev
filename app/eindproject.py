from fastapi import Depends, FastAPI, HTTPException
from random import randint
from pydantic import BaseModel
import json
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import os
import crud
import models
import schemas
from database import SessionLocal, engine
import auth


if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://127.0.0.1:5500"
    "https://localhost.tiangolo.com",
    "https://thibaudwagemans.github.io",
    "http://thibaudwagemans.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#test get hello world
@app.get("/")
async def root():
    return {"message : Hello World"}

#return all graphic cards
@app.get("/GPUs")
async def get_GPUs(db: Session = Depends(get_db)):
    return crud.get_GPUs(db)

#return a random graphic card
@app.get("/GPUs/random")
async def get_random_GPU(db: Session = Depends(get_db)):
    return crud.get_random_GPU(db)

#return a graphic card by name
@app.get("/GPUs/")
async def get_GPU(name: str, db: Session = Depends(get_db)):
    return crud.get_GPU(db, name)

#return a graphic card by closest price
@app.get("/GPUs/price/")
async def get_GPU_by_closest_price(price: int, db: Session = Depends(get_db)):
    return crud.get_gpu_by_closest_price(db, price)

#return a graphic card by closest memory
@app.get("/GPUs/memory/")
async def get_GPU_by_closest_memory(memory: int, db: Session = Depends(get_db)):
    return crud.get_gpu_by_closest_memory(db, memory)

#return a graphic card by closest power
@app.get("/GPUs/power/")
async def get_GPU_by_closest_power(power: int, db: Session = Depends(get_db)):
    return crud.get_gpu_by_closest_power(db, power)

#post a new graphic card
@app.post("/GPUs")
async def create_gpu(GPU: schemas.GPUs, db: Session = Depends(get_db)):
    return crud.create_gpu(db, GPU)

#update a graphic card by name
@app.put("/update_GPU/")
async def update_GPU(GPU: schemas.GPUs, db: Session = Depends(get_db)):
    return crud.update_gpu(db, GPU)

#delete a graphic card by name
@app.delete("/delete_GPU/")
async def delete_GPU(name: str, db: Session = Depends(get_db)):
    return crud.delete_GPU(db, name)

#post a new user
@app.post("/createusers")
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

#get all users
@app.get("/users")
async def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

#delete user
@app.delete("/delete_user/")
async def delete_user(username: str, db: Session = Depends(get_db)):
    return crud.delete_user(db, username)

#post a new release date
@app.post("/createReleaseDate")
async def create_release_date(releaseDate: schemas.releaseDate, db: Session = Depends(get_db)):
    return crud.create_release_date(db, releaseDate)

#get all release dates
@app.get("/releaseDates")
async def get_release_dates(db: Session = Depends(get_db)):
    return crud.get_release_dates(db)

#delete release date
@app.delete("/delete_releaseDate/")
async def delete_release_date(name: str, db: Session = Depends(get_db)):
    return crud.delete_release_date(db, name)
