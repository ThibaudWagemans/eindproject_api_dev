from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class GPUs(Base):
    __tablename__ = "GPUs"

    name = Column(String, primary_key=True, index=True)
    price = Column(Integer, index=True)
    memory = Column(Integer, index=True)
    power = Column(Integer, index=True)

    releaseDate = relationship("releaseDate", back_populates="GPUs")


class releaseDate(Base):
    __tablename__ = "releaseDate"

    name = Column(String, ForeignKey("GPUs.name"))
    date = Column(String, primary_key=True, index=True)

    GPUs = relationship("GPUs", back_populates="releaseDate")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

