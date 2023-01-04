from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "GPUs"
    
    name = Column(String, index=True)
    price = Column(Integer, index=True)
    memory = Column(Integer, index=True)
    power = Column(Integer, index=True)
