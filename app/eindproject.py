from fastapi import Depends, FastAPI, HTTPException
from random import randint
from pydantic import BaseModel
import json
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
import os

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
async def get_GPU_by_name(name: str, db: Session = Depends(get_db)):
    return crud.get_GPU_by_name(db, name)

#return a graphic card by closest price
@app.get("/GPUs/price/")
async def get_GPU_by_closest_price(price: int, db: Session = Depends(get_db)):
    return crud.get_GPU_by_closest_price(db, price)

#return a graphic card by closest memory
@app.get("/GPUs/memory/")
async def get_GPU_by_closest_memory(memory: int, db: Session = Depends(get_db)):
    return crud.get_GPU_by_closest_memory(db, memory)

#return a graphic card by closest power
@app.get("/GPUs/power/")
async def get_GPU_by_closest_power(power: int, db: Session = Depends(get_db)):
    return crud.get_GPU_by_closest_power(db, power)

#post a new graphic card
@app.post("/GPUs")
async def create_gpu(GPU: schemas.GPUs, db: Session = Depends(get_db)):
    return crud.create_gpu(db, GPU)

#update a graphic card by name
@app.put("/GPUs/")
async def update_GPU_by_name(name: str, GPU: schemas.GPUs, db: Session = Depends(get_db)):
    return crud.update_GPU_by_name(db, name, GPU)

#delete a graphic card by name
@app.delete("/GPUs/")
async def delete_GPU_by_name(name: str, db: Session = Depends(get_db)):
    return crud.delete_GPU_by_name(db, name)

#post a new user
@app.post("/users")
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

#get all users
@app.get("/users")
async def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
