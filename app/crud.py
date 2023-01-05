from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

#import models
#import schemas
from app import models, schemas


def get_GPUs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.GPUs).offset(skip).limit(limit).all()

def get_random_GPU(db: Session):
    return db.query(models.GPUs).order_by(func.random()).first()

def get_GPU(db: Session, name: str):
    return db.query(models.GPUs).filter(models.GPUs.name == name).first()

# def get_gpu(db: Session, gpu_id: int):
#     return db.query(models.GPUs).filter(models.GPUs.id == gpu_id).first()

def get_gpu_by_name(db: Session, name: str):
    return db.query(models.GPUs).filter(models.GPUs.name == name).first()

# def get_gpu_by_price(db: Session, price: int):
#     return db.query(models.GPUs).filter(models.GPUs.price == price).first()

def get_gpu_by_closest_price(db: Session, price: int):
    closest = db.query(models.GPUs).first()
    for GPU in db.query(models.GPUs).all():
        if abs(GPU.price - price) < abs(closest.price - price):
            closest = GPU
    return closest

# def get_gpu_by_memory(db: Session, memory: int):
#     return db.query(models.GPUs).filter(models.GPUs.memory == memory).first()

def get_gpu_by_closest_memory(db: Session, memory: int):
    closest = db.query(models.GPUs).first()
    for GPU in db.query(models.GPUs).all():
        if abs(GPU.memory - memory) < abs(closest.memory - memory):
            closest = GPU
    return closest

# def get_gpu_by_power(db: Session, power: int):
#     return db.query(models.GPUs).filter(models.GPUs.power == power).first()

def get_gpu_by_closest_power(db: Session, power: int):
    closest = db.query(models.GPUs).first()
    for GPU in db.query(models.GPUs).all():
        if abs(GPU.power - power) < abs(closest.power - power):
            closest = GPU
    return closest

def create_gpu(db: Session, gpu: schemas.GPUs):
    db_gpu = models.GPUs(name=gpu.name, price=gpu.price, memory=gpu.memory, power=gpu.power)
    db.add(db_gpu)
    db.commit()
    db.refresh(db_gpu)
    return db_gpu

def update_gpu(db: Session, gpu: schemas.GPUs):
    db_gpu = db.query(models.GPUs).filter(models.GPUs.name == gpu.name).first()
    db_gpu.price = gpu.price
    db_gpu.memory = gpu.memory
    db_gpu.power = gpu.power
    db.commit()
    db.refresh(db_gpu)
    return db_gpu

#function to delete a graphic card
def delete_GPU(name: str):
    for GPU in GPUs:
        if GPU.name == name:
            GPUs.remove(GPU)
            return GPU
    return {"error": "GPU not found"}

#funtion add user
def create_user(db: Session, user: schemas.User):
    hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=user.username, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#function get all users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

#function delete user
def delete_user(db: Session, user: schemas.User):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    db.delete(db_user)
    db.commit()
    return db_user

#function add release date
def create_release_date(db: Session, release_date: schemas.releaseDate):
    db_release_date = models.releaseDate(name=release_date.name, date=release_date.date)
    db.add(db_release_date)
    db.commit()
    db.refresh(db_release_date)
    return db_release_date

#function get all release dates
def get_release_dates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.releaseDate).offset(skip).limit(limit).all()

#function delete release date
def delete_release_date(db: Session, release_date: schemas.releaseDate):
    db_release_date = db.query(models.releaseDate).filter(models.releaseDate.name == release_date.name).first()
    db.delete(db_release_date)
    db.commit()
    return db_release_date

