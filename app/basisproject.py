from fastapi import FastAPI
from random import randint
from pydantic import BaseModel

app = FastAPI()


#class for graphic cards
class GraphicCard (BaseModel) :
    name    = str
    price   = int
    memory  = int
    power   = int

#list of graphic cards
GPUs = []

#make database graphic cards
@app.on_event("startup")
async def startup_event():
    GPUs.append(GraphicCard(name="RTX 3080", price=700, memory=10, power=350))
    GPUs.append(GraphicCard(name="RTX 3090", price=1500, memory=24, power=350))
    GPUs.append(GraphicCard(name="RTX 3070", price=500, memory=8, power=220))
    GPUs.append(GraphicCard(name="RTX 3060", price=300, memory=6, power=170))
    GPUs.append(GraphicCard(name="RTX 3050", price=200, memory=4, power=120))

#return all graphic cards
@app.get("/GPUs")
async def get_GPUs():
    return GPUs

#return a random graphic card
@app.get("/GPUs/random")
async def get_random_GPU():
    return GPUs[randint(0, len(GPUs)-1)]

#return a graphic card by name
@app.get("/GPUs/{name}")
async def get_GPU_by_name(name: str):
    for GPU in GPUs:
        if GPU.name == name:
            return GPU
    return {"error": "GPU not found"}

#return a graphic card by price
@app.get("/GPUs/price/{price}")
async def get_GPU_by_price(price: int):
    for GPU in GPUs:
        if GPU.price == price:
            return GPU
    return {"error": "GPU not found"}

#return a graphic card by memory
@app.get("/GPUs/memory/{memory}")
async def get_GPU_by_memory(memory: int):
    for GPU in GPUs:
        if GPU.memory == memory:
            return GPU
    return {"error": "GPU not found"}

#return a graphic card by power
@app.get("/GPUs/power/{power}")
async def get_GPU_by_power(power: int):
    for GPU in GPUs:
        if GPU.power == power:
            return GPU
    return {"error": "GPU not found"}

#get list graphic cards
@app.get("/GPUs")
async def get_GPUs():
    return GPUs


#function to add a graphic card
@app.post("/add")
async def add (name: str, price: int, memory: int, power: int):
    newGPU = GraphicCard(name, price, memory, power)
    GPUs.append(newGPU)
    return GPUs
