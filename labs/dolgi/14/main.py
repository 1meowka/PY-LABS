from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import func

# Создание соединения с базой данных SQLite
engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# Определение моделей
class Food(Base):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    animals = relationship('Animal', back_populates='food')

class Animal(Base):
    __tablename__ = 'animal'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    food_id = Column(Integer, ForeignKey('food.id'))
    food = relationship('Food', back_populates='animals')

# Создание таблиц в базе данных
Base.metadata.create_all()

# Заполнение базы данных
food1 = Food(name='Корм1', price=100)
food2 = Food(name='Корм2', price=150)
session.add_all([food1, food2])
session.commit()

animal1 = Animal(name='Животное1', birth_date='2022-01-01', gender='М', food=food1)
animal2 = Animal(name='Животное2', birth_date='2022-02-02', gender='Ж', food=food2)
session.add_all([animal1, animal2])
session.commit()

# Запросы
query1 = session.query(Animal.name, Animal.gender, Animal.birth_date, Food.name.label('food_name'), Food.price.label('food_price')) \
    .join(Food).all()
for result in query1:
    print(result)

query2 = session.query(Food.name, func.count(Animal.id).label('count')) \
    .join(Animal).group_by(Food.id).all()
for result in query2:
    print(result)
