from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb
import app.database.requests as rq

router = Router()


@router.message(CommandStart()) # Команда старт
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id) # Передаем айди юзера в функцию записи в бд
    await message.answer('Добро пожаловать в магазин кроссовок!', reply_markup=kb.main)


@router.message(F.text == 'Каталог') # Реагируем на слово каталог
async def catalog(message: Message): # Принимаем сообщение
    await message.answer('Выберите категорию товара', reply_markup=await kb.categories()) # возвращаем клавиатуру категорий


@router.callback_query(F.data.startswith('category_')) # Реагируем на слово category
async def category(callback: CallbackQuery): # Принимаем калбэк
    await callback.answer('Вы выбрали категорию') # Ответ
    await callback.message.answer('Выберите товар по категории',
                                  reply_markup=await kb.items(callback.data.split('_')[1])) # вернуть клавиатуру


@router.callback_query(F.data.startswith('item_')) # Реагируем на слово item
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали товар')
    await callback.message.answer(f'Название: {item_data.name}\nОписание: {item_data.description}\nЦена: {item_data.price}$')