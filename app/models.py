from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class GPUs(Base):
    __tablename__ = "GPUs"

    name = Column(String, primary_key=True, index=True)
    price = Column(Integer, index=True)
    memory = Column(Integer, index=True)
    power = Column(Integer, index=True)

    releaseDates = relationship("releaseDates", back_populates="GPUs")


class releaseDates(Base):
    __tablename__ = "releaseDates"

    name = Column(String, ForeignKey("GPUs.name"))
    date = Column(String, primary_key=True, index=True)
    GPU = relationship("GPUs", back_populates="releaseDates")

    GPUs = relationship("GPUs", back_populates="releaseDates")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

