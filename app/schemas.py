from pydantic import BaseModel


#classes van users
class User (BaseModel) :
    username: str
    password: str

class Usercreate (User) :
    pass

class delete_user (User) :
    pass

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
    pass


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



