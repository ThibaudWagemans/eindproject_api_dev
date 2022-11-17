from fastapi import FastAPI
from random import randint
from pydantic import BaseModel
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5500"
    "https://thibaudwagemans.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "DELETE"],
    allow_headers=["*"],
)

#class for graphic cards
class GraphicCard (BaseModel) :
    name    : str
    price   : int
    memory  : int
    power   : int

#list of graphic cards
GPUs = []

#make database graphic cards
GPUs.append(GraphicCard(name="RTX 3080", price=700, memory=10, power=350))
GPUs.append(GraphicCard(name="RTX 3090", price=1500, memory=24, power=350))
GPUs.append(GraphicCard(name="RTX 3070", price=500, memory=8, power=220))
GPUs.append(GraphicCard(name="RTX 3060", price=300, memory=6, power=170))
GPUs.append(GraphicCard(name="RTX 3050", price=200, memory=4, power=120))

#test get hello world
@app.get("/")
async def root():
    return {"message : Hello World"}

#return all graphic cards
@app.get("/GPUs")
async def get_GPUs():
    return GPUs

#return a random graphic card
@app.get("/GPUs/random")
async def get_random_GPU():
    return GPUs[randint(0, len(GPUs)-1)]

#return a graphic card by name
@app.get("/GPUs/")
async def get_GPU_by_name(name: str):
    for GPU in GPUs:
        if GPU.name == name:
            return GPU
    return {"error": "GPU not found"}

#return a graphic card by price
#@app.get("/GPUs/price/{price}")
#async def get_GPU_by_price(price: int):
#    for GPU in GPUs:
#        if GPU.price == price:
#            return GPU
#    return {"error": "GPU not found"}

#return a graphic card by closest price
@app.get("/GPUs/price/")
async def get_GPU_by_closest_price(price: int):
    closest = GPUs[0]
    for GPU in GPUs:
        if abs(GPU.price - price) < abs(closest.price - price):
            closest = GPU
    return closest

#return a graphic card by memory
#@app.get("/GPUs/memory/{memory}")
#async def get_GPU_by_memory(memory: int):
#    for GPU in GPUs:
#        if GPU.memory == memory:
#            return GPU
#    return {"error": "GPU not found"}

#return a graphic card by closest memory
@app.get("/GPUs/memory/")
async def get_GPU_by_closest_memory(memory: int):
    closest = GPUs[0]
    for GPU in GPUs:
        if abs(GPU.memory - memory) < abs(closest.memory - memory):
            closest = GPU
    return closest

#return a graphic card by power
#@app.get("/GPUs/power/{power}")
#async def get_GPU_by_power(power: int):
#    for GPU in GPUs:
#        if GPU.power == power:
#            return GPU
#    return {"error": "GPU not found"}

#return a graphic card by closest power
@app.get("/GPUs/power/")
async def get_GPU_by_closest_power(power: int):
    closest = GPUs[0]
    for GPU in GPUs:
        if abs(GPU.power - power) < abs(closest.power - power):
            closest = GPU
    return closest

#function to add a graphic card
@app.post("/add/")
async def add (name: str, price: int, memory: int, power: int):
    #check if the graphic card already exists
    for GPU in GPUs:
        if GPU.name == name:
            return {"error": "GPU already exists"}
    newGPU = GraphicCard(name = name, price = price, memory = memory, power = power)
    GPUs.append(newGPU)
    return newGPU

#function to delete a graphic card
@app.delete("/delete/")
async def delete (name: str):
    for GPU in GPUs:
        if GPU.name == name:
            GPUs.remove(GPU)
            return GPU
    return {"error": "GPU not found"}

#function to update a graphic card
@app.put("/update/")
async def update (name: str, price: int, memory: int, power: int):
    for GPU in GPUs:
        if GPU.name == name:
            GPU.price = price
            GPU.memory = memory
            GPU.power = power
            return GPU
    return {"error": "GPU not found"}
from fastapi import FastAPI
from random import randint
from pydantic import BaseModel
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#class for graphic cards
class GraphicCard (BaseModel) :
    name    : str
    price   : int
    memory  : int
    power   : int

#list of graphic cards
GPUs = []

#make database graphic cards
GPUs.append(GraphicCard(name="RTX 3080", price=700, memory=10, power=350))
GPUs.append(GraphicCard(name="RTX 3090", price=1500, memory=24, power=350))
GPUs.append(GraphicCard(name="RTX 3070", price=500, memory=8, power=220))
GPUs.append(GraphicCard(name="RTX 3060", price=300, memory=6, power=170))
GPUs.append(GraphicCard(name="RTX 3050", price=200, memory=4, power=120))

#test get hello world
@app.get("/")
async def root():
    return {"message : Hello World"}

#return all graphic cards
@app.get("/GPUs")
async def get_GPUs():
    return GPUs

#return a random graphic card
@app.get("/GPUs/random")
async def get_random_GPU():
    return GPUs[randint(0, len(GPUs)-1)]

#return a graphic card by name
@app.get("/GPUs/")
async def get_GPU_by_name(name: str):
    for GPU in GPUs:
        if GPU.name == name:
            return GPU
    return {"error": "GPU not found"}

#return a graphic card by price
#@app.get("/GPUs/price/{price}")
#async def get_GPU_by_price(price: int):
#    for GPU in GPUs:
#        if GPU.price == price:
#            return GPU
#    return {"error": "GPU not found"}

#return a graphic card by closest price
@app.get("/GPUs/price/")
async def get_GPU_by_closest_price(price: int):
    closest = GPUs[0]
    for GPU in GPUs:
        if abs(GPU.price - price) < abs(closest.price - price):
            closest = GPU
    return closest

#return a graphic card by memory
#@app.get("/GPUs/memory/{memory}")
#async def get_GPU_by_memory(memory: int):
#    for GPU in GPUs:
#        if GPU.memory == memory:
#            return GPU
#    return {"error": "GPU not found"}

#return a graphic card by closest memory
@app.get("/GPUs/memory/")
async def get_GPU_by_closest_memory(memory: int):
    closest = GPUs[0]
    for GPU in GPUs:
        if abs(GPU.memory - memory) < abs(closest.memory - memory):
            closest = GPU
    return closest

#return a graphic card by power
#@app.get("/GPUs/power/{power}")
#async def get_GPU_by_power(power: int):
#    for GPU in GPUs:
#        if GPU.power == power:
#            return GPU
#    return {"error": "GPU not found"}

#return a graphic card by closest power
@app.get("/GPUs/power/")
async def get_GPU_by_closest_power(power: int):
    closest = GPUs[0]
    for GPU in GPUs:
        if abs(GPU.power - power) < abs(closest.power - power):
            closest = GPU
    return closest

#function to add a graphic card
@app.post("/add/")
async def add (name: str, price: int, memory: int, power: int):
    #check if the graphic card already exists
    for GPU in GPUs:
        if GPU.name == name:
            return {"error": "GPU already exists"}
    newGPU = GraphicCard(name = name, price = price, memory = memory, power = power)
    GPUs.append(newGPU)
    return newGPU

#function to delete a graphic card
@app.delete("/delete/")
async def delete (name: str):
    for GPU in GPUs:
        if GPU.name == name:
            GPUs.remove(GPU)
            return GPU
    return {"error": "GPU not found"}

#function to update a graphic card
@app.put("/update/")
async def update (name: str, price: int, memory: int, power: int):
    for GPU in GPUs:
        if GPU.name == name:
            GPU.price = price
            GPU.memory = memory
            GPU.power = power
            return GPU
    return {"error": "GPU not found"}
