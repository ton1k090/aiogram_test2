from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3') # создание БД

async_session = async_sessionmaker(engine) # Подключение к БД


class Base(AsyncAttrs, DeclarativeBase):
    '''Класс дает возможность с помощью него
    управлять всеми его дочерними классами'''
    pass


class User(Base):
    '''Класс пользователя'''
    __tablename__ = 'users' # название таблицы во множественном числе

    id: Mapped[int] = mapped_column(primary_key=True) # id в таблице
    tg_id = mapped_column(BigInteger) # уникальное значение пользователя


class Category(Base):
    '''Класс категорий'''
    __tablename__ = 'categories' # название таблицы во множественном числе

    id: Mapped[int] = mapped_column(primary_key=True) # айди
    name: Mapped[str] = mapped_column(String(25))  # название категории


class Item(Base):
    '''Класс товара'''
    __tablename__ = 'items' # название таблицы во множественном числе

    id: Mapped[int] = mapped_column(primary_key=True) # айди в таблице
    name: Mapped[str] = mapped_column(String(25)) # Название
    description: Mapped[str] = mapped_column(String(120)) # Описание
    price: Mapped[int] = mapped_column() # Цена
    category: Mapped[int] = mapped_column(ForeignKey('categories.id')) # Связать с категорией


async def async_main():
    '''Создаем все таблицы и запускаем сессию'''
    async with engine.begin() as conn: # Начать сессию
        await conn.run_sync(Base.metadata.create_all) # Используя подключение запустить синхронизацию