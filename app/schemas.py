from pydantic import BaseModel


#classes van users
class User (BaseModel) :
    username: str
    password: str

class Usercreate (User) :
    pass

class delete_user (User) :
    username : str

#classes van GPUs
class GPUs (BaseModel) :
    name: str
    price: int
    memory: int
    power: int

class addGraphicCard (GPUs) :
    pass

class updateGraphicCard (BaseModel) :
    price: int
    memory: int
    power: int

class deleteGraphicCard (GPUs) :
    name : str


#classes van releaseDates
class releaseDate (BaseModel) :
    name: str
    date: str

class addReleaseDate (releaseDate) :
    pass

class updateReleaseDate (releaseDate) :
    pass

class deleteReleaseDate (releaseDate) :
    name: str



