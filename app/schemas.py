from pydantic import BaseModel


#classes van users
class User (BaseModel) :
    username: str


class Usercreate (User) :
    password: str

class delete_user (User) :
    pass

#classes van GPUs
class GPUsBase (BaseModel) :
    name: str

class GPUs (GPUsBase) :
    price: int
    memory: int
    power: int

class addGraphicCard (GPUsBase) :
    price: int
    memory: int
    power: int

class updateGraphicCard (GPUsBase) :
    price: int
    memory: int
    power: int

class deleteGraphicCard (GPUsBase) :
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



