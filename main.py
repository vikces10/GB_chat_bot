import asyncio
import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import logging
import random

#Логирование
logging.basicConfig(level=logging.INFO)

# Объект бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')

@dp.message(Command(commands=['user']))
async def user(message: types.Message):
    await message.answer(f'Ваш username: {message.from_user.username}.')

@dp.message(Command(commands=['id']))
async def id(message: types.Message):
    await message.answer(f'Ваш ID: {message.from_user.id}')

@dp.message(Command(commands=['info']))
async def info(message: types.Message):
    await message.answer("Я бот - твой друг и товарищ 😊")

@dp.message(Command(commands=['joke']))
async def joke(message: types.Message):
    await message.answer("Анекдот: Программа получилась плохой, а сроки горят, и заказчик ругается! Не волнуйтесь, смело выпускайте релиз. Просто назовите его версией 1.0. 😂😂😂")

@dp.message(Command(commands=['stop']))
async def stop(message: types.Message):
    await message.answer(f'Пока, {message.from_user.full_name}!')

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
