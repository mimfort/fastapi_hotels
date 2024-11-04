from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from app.database import Base


class Hotels(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String, nullable=False)

    location: Mapped[str] = mapped_column(String, nullable=False)

    services: Mapped[dict] = mapped_column(JSON)

    rooms_quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    image_id: Mapped[int] = mapped_column(Integer)

