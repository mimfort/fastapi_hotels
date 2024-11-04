from datetime import date

from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from app.database import Base


class Rooms(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)

    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"), nullable=False)

    name: Mapped[str] = mapped_column(String, nullable=False)

    description: Mapped[str] = mapped_column(String, nullable=True)

    price: Mapped[int] = mapped_column(Integer, nullable=False)

    services: Mapped[dict] = mapped_column(JSON, nullable=True)

    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    image_id: Mapped[int] = mapped_column(Integer)

