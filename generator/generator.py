from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')


def generate_person():
    yield Person(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.email()
    )
