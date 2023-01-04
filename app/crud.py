from sqlalchemy.orm import Session

import models
import schemas


def get_GPUs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.GraphicCard).offset(skip).limit(limit).all()

# def get_gpu(db: Session, gpu_id: int):
#     return db.query(models.GraphicCard).filter(models.GraphicCard.id == gpu_id).first()

def get_gpu_by_name(db: Session, name: str):
    return db.query(models.GraphicCard).filter(models.GraphicCard.name == name).first()

# def get_gpu_by_price(db: Session, price: int):
#     return db.query(models.GraphicCard).filter(models.GraphicCard.price == price).first()

def get_gpu_by_closest_price(db: Session, price: int):
    closest = db.query(models.GraphicCard).first()
    for GPU in db.query(models.GraphicCard).all():
        if abs(GPU.price - price) < abs(closest.price - price):
            closest = GPU
    return closest

# def get_gpu_by_memory(db: Session, memory: int):
#     return db.query(models.GraphicCard).filter(models.GraphicCard.memory == memory).first()

def get_gpu_by_closest_memory(db: Session, memory: int):
    closest = db.query(models.GraphicCard).first()
    for GPU in db.query(models.GraphicCard).all():
        if abs(GPU.memory - memory) < abs(closest.memory - memory):
            closest = GPU
    return closest

# def get_gpu_by_power(db: Session, power: int):
#     return db.query(models.GraphicCard).filter(models.GraphicCard.power == power).first()

def get_gpu_by_closest_power(db: Session, power: int):
    closest = db.query(models.GraphicCard).first()
    for GPU in db.query(models.GraphicCard).all():
        if abs(GPU.power - power) < abs(closest.power - power):
            closest = GPU
    return closest

def create_gpu(db: Session, gpu: schemas.GraphicCard):
    db_gpu = models.GraphicCard(name=gpu.name, price=gpu.price, memory=gpu.memory, power=gpu.power)
    db.add(db_gpu)
    db.commit()
    db.refresh(db_gpu)
    return db_gpu

def update_gpu(db: Session, gpu: schemas.GraphicCard):
    db_gpu = db.query(models.GraphicCard).filter(models.GraphicCard.name == gpu.name).first()
    db_gpu.price = gpu.price
    db_gpu.memory = gpu.memory
    db_gpu.power = gpu.power
    db.commit()
    db.refresh(db_gpu)
    return db_gpu

#function to delete a graphic card
def delete_GPU_by_name(name: str):
    for GPU in GPUs:
        if GPU.name == name:
            GPUs.remove(GPU)
            return GPU
    return {"error": "GPU not found"}

# #function to delete a graphic card
# def delete_GPU(id: int):
#     for GPU in GPUs:
#         if GPU.id == id:
#             GPUs.remove(GPU)
#             return GPU
#     return {"error": "GPU not found"}


