import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
from aiogram import types
import random
from keyboards import keyboard

#Логирование
logging.basicConfig(level=logging.INFO)

# Объект бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=keyboard)

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


@dp.message(F.text.lower() == "число")
async def number (message: types.Message):
    number = random.randint(a=0,b=100)
    await message.answer(f'Твое число {number}!')

@dp.message(F.text)
async def msg (message: types.Message):
    if "привет" in message.text.lower():
        await message.reply('И тебе привет!')
    elif "как дела" in message.text.lower():
        await message.reply('Нормально, а у тебя?')
    elif "хорошо" in message.text.lower():
        await message.reply('Рад за тебя!')
    elif "ок" in message.text.lower():
        await message.reply('Рад это слышать!')
    elif "отлично" in message.text.lower():
        await message.reply('Класс!')
    elif "плохо" in message.text.lower():
        await message.reply('Не переживай, все наладится!')
    else:
        await message.reply('Не понимаю тебя...')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

