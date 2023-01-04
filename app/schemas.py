from pydantic import BaseModel

class GraphicCard (BaseModel) :
    name: str
    price: int
    memory: int
    power: int

class User (BaseModel) :
    username: str
    password: str

class GraphicCard (GraphicCard) :
    name: str
    price: int
    memory: int
    power: int

class User (User) :
    username: str
    password: str

class updateGraphicCard (BaseModel) :
    name: str
    price: int
    memory: int
    power: int

class deleteGraphicCard (BaseModel) :
    name: str

class addGraphicCard (BaseModel) :
    name: str
    price: int
    memory: int
    power: int

class updateGraphicCard (updateGraphicCard) :
    name: str
    price: int
    memory: int
    power: int

class deleteGraphicCard (deleteGraphicCard) :
    name: str

class addGraphicCard (addGraphicCard) :
    name: str
    price: int
    memory: int
    power: int


