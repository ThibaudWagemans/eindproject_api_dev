from pydantic import BaseModel


#classes van users
class User (BaseModel) :
    username: str
    password: str

class Usercreate (User) :
    pass

#classes van GPUs
class GPUs (BaseModel) :
    name: str
    price: int
    memory: int
    power: int

class addGraphicCard (GPUs) :
    pass

class updateGraphicCard (GPUs) :
    pass

class deleteGraphicCard (BaseModel) :
    name: str


#classes van releaseDates
class releaseDate (BaseModel) :
    name: str
    date: str

class addReleaseDate (releaseDate) :
    pass

class updateReleaseDate (releaseDate) :
    pass

class deleteReleaseDate (BaseModel) :
    name: str
    date: str



