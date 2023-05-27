from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


# Создание подключения к базе данных
engine = create_engine('sqlite:///database.db', echo=True)  # Замените 'sqlite:///database.db' на свою строку подключения

# Создание объекта сессии для взаимодействия с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Определение базовой модели
Base = declarative_base()


# Модель Корма
class Food(Base):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True)
    kind = Column(String)
    manufacturer = Column(String)
    name = Column(String)
    price = Column(Integer)

    animals = relationship("Animal", back_populates="food")

    def __repr__(self):
        return f"<Food(name='{self.name}', price={self.price})>"


# Модель Животного
class Animal(Base):
    __tablename__ = 'animal'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    food_id = Column(Integer, ForeignKey('food.id'))

    food = relationship("Food", back_populates="animals")

    def __repr__(self):
        return f"<Animal(name='{self.name}', gender='{self.gender}')>"


# Модель Вида животного
class AnimalType(Base):
    __tablename__ = 'animal_type'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"<AnimalType(name='{self.name}')>"

