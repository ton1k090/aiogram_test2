from app.database.models import async_session
from app.database.models import User, Category, Item
from sqlalchemy import select


async def set_user(tg_id: int) -> None: # Передается айди юзера
    '''Записывает пользователя в БД'''
    async with async_session() as session: # Начать сессию
        user = await session.scalar(select(User).where(User.tg_id == tg_id)) # Возвращает юзера по айди

        if not user: # Если нет юзера
            session.add(User(tg_id=tg_id)) # Добавляем юзера в БД
            await session.commit() # фиксируем изменения


async def get_categories():
    '''Достать из БД все категории'''
    async with async_session() as session: # Начать сессию
        return await session.scalars(select(Category)) # Достать категории


async def get_category_item(category_id):
    ''''''
    async with async_session() as session: # Начать сессию
        return await session.scalars(select(Item).where(Item.category == category_id))


async def get_item(item_id):
    async with async_session() as session: # Начать сессию
        return await session.scalar(select(Item).where(Item.id == item_id))