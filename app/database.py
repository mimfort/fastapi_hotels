from sqlalchemy.ext.asyncio import  create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "postgres"
DB_PASS = "Legogi142005"
DB_NAME = "postgres"
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Создаем асинхронный движок
engine = create_async_engine(DATABASE_URL, echo=True)

# Создаем фабрику для асинхронной сессии
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)

# Базовый класс для ORM
class Base(DeclarativeBase):
    pass
