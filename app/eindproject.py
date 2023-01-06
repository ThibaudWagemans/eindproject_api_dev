from fastapi import Depends, FastAPI, HTTPException, status
from random import randint
from pydantic import BaseModel
import json
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBasic, HTTPBasicCredentials


from app import crud, models, schemas, auth
import os
#import crud
#import models
#import schemas
#import auth
from app.database import SessionLocal, engine

print("We are in the main.......")
if not os.path.exists('.\sqlitedb'):
    print("Making folder.......")
    os.makedirs('.\sqlitedb')

print("Creating tables.......")
#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)
print("Tables created.......")


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    #Try to authenticate the user
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = auth.create_access_token(
        data={"sub": user.username}
    )
    #Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}


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
@app.get("/GPU")
async def get_GPU(name: str, db: Session = Depends(get_db)):
    return crud.get_GPU(db, name)

#return a graphic card by closest price
@app.get("/GPUs/price")
async def get_GPU_by_closest_price(price: int, db: Session = Depends(get_db)):
    return crud.get_gpu_by_closest_price(db, price)

#return a graphic card by closest memory
@app.get("/GPUs/memory")
async def get_GPU_by_closest_memory(memory: int, db: Session = Depends(get_db)):
    return crud.get_gpu_by_closest_memory(db, memory)

#return a graphic card by closest power
@app.get("/GPUs/power")
async def get_GPU_by_closest_power(power: int, db: Session = Depends(get_db)):
    return crud.get_gpu_by_closest_power(db, power)

#post a new graphic card
@app.post("/GPUs")
async def create_gpu(GPU: schemas.GPUs, db: Session = Depends(get_db)):
    return crud.create_gpu(db, GPU)

#update a graphic card by name
@app.put("/update_GPU")
async def update_GPU(GPU: schemas.GPUs, db: Session = Depends(get_db)):
    return crud.update_gpu(db, GPU)

#delete a graphic card by name
@app.delete("/delete_GPU")
async def delete_GPU(GPU: schemas.deleteGraphicCard, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.delete_gpu(db, GPU)

#post a new user
@app.post("/createusers")
async def create_user(user: schemas.Usercreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

#get all users
@app.get("/users")
async def get_users(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.get_users(db)

#delete user
@app.delete("/delete_user")
async def delete_user(user: schemas.delete_user, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.delete_user(db, user)

#post a new release date
@app.post("/createReleaseDate")
async def create_release_date(releaseDate: schemas.releaseDate, db: Session = Depends(get_db)):
    return crud.create_release_date(db, releaseDate)

#get all release dates
@app.get("/releaseDates")
async def get_release_dates(db: Session = Depends(get_db)):
    return crud.get_release_dates(db)

#delete release date
@app.delete("/delete_releaseDate")
async def delete_release_date(releaseDate: schemas.deleteReleaseDate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.delete_release_date(db, releaseDate)
