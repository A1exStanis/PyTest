from typing import Optional
from pydantic import BaseModel, Field


class CarSchema(BaseModel):
    id: Optional[int] = Field(default=1)
    title: str = Field(default="Car")
    state: str = Field(default="Factory new")
    owner: str = Field(default="IT specialist")

    class Config:
        from_attributes = True

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        for attr in ["title", "state", "owner"]:
            if getattr(self, attr) != getattr(other, attr):
                return False
        return True

    def to_dict_wo_id(self) -> dict:
        return self.model_dump(exclude={"id"})
