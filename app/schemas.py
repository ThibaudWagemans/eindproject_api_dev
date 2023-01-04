from pydantic import BaseModel

class GraphicCard (BaseModel) :
    name: str
    price: int
    memory: int
    power: int
