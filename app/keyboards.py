from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_categories, get_category_item

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контакты'),
                                      KeyboardButton(text='О нас')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')


async def categories():
    all_categories = await get_categories() # Импортировать функцию из запросов
    keyboard = InlineKeyboardBuilder() # создать клавиатуру
    for category in all_categories: # перебрать все категории
        keyboard.add(InlineKeyboardButton(
            text=category.name,
            callback_data=f"category_{category.id}")) # Ловить все калбэки начинающиеся с category
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main')) # Кнопка на главную
    return keyboard.adjust(2).as_markup() # кнопки по 2 в строке


async def items(category_id):
    all_items = await get_category_item(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f"item_{item.id}"))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()