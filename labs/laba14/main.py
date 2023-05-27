from datetime import datetime
from models import Food, Species, Animal
from database import session


Species.__table__.create(bind=session.bind, checkfirst=True)
Food.__table__.create(bind=session.bind, checkfirst=True)
Animal.__table__.create(bind=session.bind, checkfirst=True)

#Заполнение БД данными
# cat_species = Species(name='Кот')
# dog_species = Species(name='Собака')
# session.add_all([cat_species, dog_species])
# session.commit()

# cat_food = Food(species=cat_species, manufacturer='Manufacturer 1', name='Китикет', price=10)
# dog_food = Food(species=dog_species, manufacturer='Manufacturer 2', name='Чаппи', price=20)
# session.add_all([cat_food, dog_food])
# session.commit()

# cat = Animal(name='Мяука', birth_date=datetime(2018, 5, 10), gender='Ж', species=cat_species)
# dog = Animal(name='Гафгалка', birth_date=datetime(2019, 3, 15), gender='М', species=dog_species)
# session.add_all([cat, dog])
# session.commit()

#Запросы
animals = session.query(Animal).all()
for animal in animals:
    print('Кличка:', animal.name)
    print('Пол:', animal.gender)
    age = datetime.now().year - animal.birth_date.year
    print('Возраст:', age)

    food = session.query(Food).filter_by(species_id=animal.species_id).first()
    print('Название корма:', food.name)
    print('Цена корма:', food.price)
    print()

foods = session.query(Food).all()
for food in foods:
    animal_count = session.query(Animal).filter_by(species_id=food.species_id).count()
    print('Название корма:', food.name)
    print('Сколько животных им питается:', animal_count)
