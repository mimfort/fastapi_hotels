from fastapi import APIRouter
from sqlalchemy import select

from app.bookings.dao import BookingDao
from app.bookings.models import Bookings
from app.database import async_session_maker
from app.bookings.dao import BookingDao

router = APIRouter(
     prefix="/bookings",
     tags = ["Бронирования"])
@router.get("")
async def get_bookings():
    async with async_session_maker() as session:
        # query  = select(Bookings.__table__.columns)
        # result = await session.execute(query)
        # return result.mappings().all()
        return await BookingDao.find_all()


