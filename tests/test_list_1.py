import pytest
from Functions.Cars.schemas import CarSchema
from Functions.Cars.service import CarService
from Functions.db import Base, engine
from Functions.Cars.models import Cars


@pytest.fixture(scope='session', autouse=True)
def setup_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@pytest.fixture
def cars():
    cars = [
        CarSchema(title='BMW'),
        CarSchema(title='Audi')
    ]
    return cars


@pytest.fixture
def empty_cars():
    CarService.delete_all()


@pytest.mark.usefixtures('empty_cars')
class TestCars:
    def test_count_cars(self, cars):
        for car in cars:
            CarService.add(car)

        assert CarService.count() == 2

    def test_list_car(self, cars):
        for car in cars:
            CarService.add(car)

        all_cars = CarService.list()
        for added_car in all_cars:
            assert added_car in cars
