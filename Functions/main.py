import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from Functions.Cars.repository import CarRepository
from Functions.Cars.schemas import CarSchema
from Functions.db import Base, engine

from Functions.Cars.service import CarService
# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)


print(" Car ".center(80, "="))

candy_1 = CarSchema(title="Ferrari", kid="None")
added_candy = CarService.add(candy_1)
all = CarService.list()
first = CarService.get(36)
print(f"{added_candy=}")
print()
print(f"{all=}")
print()
print(f"{first=}")