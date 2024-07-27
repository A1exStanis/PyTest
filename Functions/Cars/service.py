from typing import Optional
from pydantic import TypeAdapter
from Functions.Cars.repository import CarRepository
from Functions.Cars.schemas import CarSchema


class CarService:
    @classmethod
    def add(cls, car: CarSchema):
        car_dict = car.to_dict_wo_id()
        new_car = CarRepository.add(car_dict)
        return TypeAdapter(CarSchema).dump_python(new_car)

    @classmethod
    def get(cls, car_id: int):
        car = CarRepository.get(car_id)
        return TypeAdapter(CarSchema).dump_python(car)

    @classmethod
    def list(
            cls,
            title: Optional[str] = None,
            state: Optional[str] = None,
            owner: Optional[str] = None,
    ):
        filter_by = {k: v for k, v in {"title": title, "state": state, "owner": owner}.items() if v}
        car = CarRepository.list(filter_by)
        return TypeAdapter(list[CarSchema]).dump_python(car)

    @classmethod
    def count(cls) -> int:
        count = CarRepository.count()
        return count

    @classmethod
    def update(cls, car_id: int, car: CarSchema):
        car_dict = car.to_dict_wo_id()
        CarRepository.update(car_id, car_dict)

    @classmethod
    def finish(cls, car_id: int):
        finish_dict = {"state": "eaten"}
        CarRepository.finish(car_id, finish_dict)

    @classmethod
    def delete(cls, car_id: int):
        CarRepository.delete(car_id)

    @classmethod
    def delete_all(cls):
        CarRepository.delete_all()
