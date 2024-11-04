from datetime import date

from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date, Computed
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from app.database import Base


class Bookings(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)

    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    date_from: Mapped[date] = mapped_column(Date, nullable=False)

    date_to: Mapped[date] = mapped_column(Date, nullable=False)

    price: Mapped[int] = mapped_column(Integer, nullable=False)

    total_cost: Mapped[int] = mapped_column(Integer, Computed("DATEDIFF(date_to - date_from) * price"))

    total_days: Mapped[int] = mapped_column(Integer, Computed("DATEDIFF(date_to - date_from)"))