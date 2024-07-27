from sqlalchemy import delete, func, insert, select, update
from Functions.db import Session

from models import Cars


class CarRepository:
    @classmethod
    def add(cls, values: dict):
        with Session() as session:
            stmt = insert(Cars).values(**values).returning(Cars)
            new_car = session.execute(stmt)
            session.commit()
            return new_car.scalar_one()

    @classmethod
    def get(cls, car_id: int):
        query = select(Cars.__table__.columns).filter_by(id=car_id)
        with Session() as session:
            candy = session.execute(query)
            session.commit()
            return candy.mappings().one()

    @classmethod
    def list(cls, filter_by: dict):
        query = select(Cars).filter_by(**filter_by)
        with Session() as session:
            cars = session.execute(query)
            session.commit()
            return cars.scalars().all()

    @classmethod
    def count(cls) -> int:
        query = select(func.count(Cars.id)).select_from(Cars)
        with Session() as session:
            cars_count = session.execute(query)
            session.commit()
            return cars_count.scalar()

    @classmethod
    def update(cls, car_id: int, values: dict):
        stmt = update(Cars).where(Cars.id == car_id).values(**values)
        with Session() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def finish(cls, car_id: int, values: dict):
        stmt = update(Cars).where(Cars.id == car_id).values(**values)
        with Session() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def delete(cls, car_id: int):
        stmt = delete(Cars).where(Cars.id == car_id)
        with Session() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def delete_all(cls):
        stmt = delete(Cars)
        with Session() as session:
            session.execute(stmt)
            session.commit()
            