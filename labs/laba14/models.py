from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Food(Base):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True)
    species_id = Column(Integer, ForeignKey('species.id'))
    manufacturer = Column(String(100))
    name = Column(String(100))
    price = Column(Integer)
    species = relationship("Species", back_populates="foods")

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    animals = relationship("Animal", back_populates="species")
    foods = relationship("Food", back_populates="species")

class Animal(Base):
    __tablename__ = 'animal'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    birth_date = Column(DateTime)
    gender = Column(String(10))
    species_id = Column(Integer, ForeignKey('species.id'))
    species = relationship("Species", back_populates="animals")
