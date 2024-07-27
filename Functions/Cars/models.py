from typing import Optional
from Functions.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Cars(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    state: Mapped[str] = mapped_column(String(20), nullable=False, server_default="Factory new")
    owner: Mapped[str] = mapped_column(String(100), nullable=False, server_default="IT specialist")
