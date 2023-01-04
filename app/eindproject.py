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
async def create_GPU(GPU: schemas.GraphicCard, db: Session = Depends(get_db)):
    return crud.create_GPU(db, GPU)

#update a graphic card by name
@app.put("/GPUs/")
async def update_GPU_by_name(name: str, GPU: schemas.GraphicCard, db: Session = Depends(get_db)):
    return crud.update_GPU_by_name(db, name, GPU)

#delete a graphic card by name
@app.delete("/GPUs/")
async def delete_GPU_by_name(name: str, db: Session = Depends(get_db)):
    return crud.delete_GPU_by_name(db, name)






















# #return all graphic cards
# @app.get("/GPUs")
# async def get_GPUs():
#     return GPUs

# #return a random graphic card
# @app.get("/GPUs/random")
# async def get_random_GPU():
#     return GPUs[randint(0, len(GPUs)-1)]

# #return a graphic card by name
# @app.get("/GPUs/")
# async def get_GPU_by_name(name: str):
#     for GPU in GPUs:
#         if GPU.name == name:
#             return GPU
#     return {"error": "GPU not found"}


# #return a graphic card by closest price
# @app.get("/GPUs/price/")
# async def get_GPU_by_closest_price(price: int):
#     closest = GPUs[0]
#     for GPU in GPUs:
#         if abs(GPU.price - price) < abs(closest.price - price):
#             closest = GPU
#     return closest

# #return a graphic card by closest memory
# @app.get("/GPUs/memory/")
# async def get_GPU_by_closest_memory(memory: int):
#     closest = GPUs[0]
#     for GPU in GPUs:
#         if abs(GPU.memory - memory) < abs(closest.memory - memory):
#             closest = GPU
#     return closest

# #return a graphic card by closest power
# @app.get("/GPUs/power/")
# async def get_GPU_by_closest_power(power: int):
#     closest = GPUs[0]
#     for GPU in GPUs:
#         if abs(GPU.power - power) < abs(closest.power - power):
#             closest = GPU
#     return closest

# #function to add a graphic card
# @app.post("/add/")
# async def add (name: str, price: int, memory: int, power: int):
#     #check if the graphic card already exists
#     for GPU in GPUs:
#         if GPU.name == name:
#             return {"error": "GPU already exists"}
#     newGPU = GraphicCard(name = name, price = price, memory = memory, power = power)
#     GPUs.append(newGPU)
#     return newGPU

# #function to delete a graphic card
# @app.delete("/delete/")
# async def delete (name: str):
#     for GPU in GPUs:
#         if GPU.name == name:
#             GPUs.remove(GPU)
#             return GPU
#     return {"error": "GPU not found"}

# #function to update a graphic card
# @app.put("/update/")
# async def update (name: str, price: int, memory: int, power: int):
#     for GPU in GPUs:
#         if GPU.name == name:
#             GPU.price = price
#             GPU.memory = memory
#             GPU.power = power
#             return GPU
#     return {"error": "GPU not found"}
