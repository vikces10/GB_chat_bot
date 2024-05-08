import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
from aiogram import types
import random
from keyboards import keyboard
from fox import fox
from fox import get_ip
from fox import coin


#Логирование
logging.basicConfig(level=logging.INFO)

# Объект бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=keyboard)

@dp.message(Command(commands=['Лиса']))
async def user(message: types.Message):
    img_fox = fox()
    await message.answer('Лови лису')
    await message.answer_photo(img_fox)
    # img_fox = fox()
    # await bot.send_photo(message.from_user.id, img_fox)

@dp.message(Command(commands=['ip']))
async def id(message: types.Message):
    ip_address = get_ip()
    await message.answer(f'Ваш IP: {ip_address}')

@dp.message(Command(commands=['число']))
async def info(message: types.Message):
    number = random.randint(a=0, b=100)
    await message.answer(f'Твое случайное число от 0 до 100: {number}!')

@dp.message(Command(commands=['BTC']))
async def coin_handler(message: types.Message):
    btc_price = coin()
    await message.answer(f'Текущая цена {btc_price}')


@dp.message(Command(commands=['игра']))
async def game(message: types.Message):
    await message.answer(f'{message.from_user.full_name}, давай поиграем! Задумай число из двух цифр')
    await asyncio.sleep(7)
    await message.answer('Прибавь к нему 7')
    await asyncio.sleep(5)
    await message.answer('От 110 отними полученную сумму')
    await asyncio.sleep(15)
    await message.answer('К ответу прибавь 15 ')
    await asyncio.sleep(10)
    await message.answer('Прибавь задуманное число')
    await asyncio.sleep(15)
    await message.answer('Полученное число раздели пополам')
    await asyncio.sleep(10)
    await message.answer('От результата отними 9')
    await asyncio.sleep(5)
    await message.answer('Умножь на 3')
    await asyncio.sleep(5)
    await message.answer('Теперь внимание! Твой ответ ....')
    await asyncio.sleep(5)
    await message.answer('150  Верно? да/нет')


@dp.message(F.text.lower() == "число")
async def number (message: types.Message):
    number = random.randint(a=0,b=100)
    await message.answer(f'Твое случайное число от 0 до 100: {number}!')

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
    elif "да" in message.text.lower():
        await message.answer('Вот такой фокус 😉 ')
    elif "нет" in message.text.lower():
        await message.answer('Возможно закралась ошибка в твоих вычислениях 🙄 Попробуй еще раз! ')
    else:
        await message.reply('Не понимаю тебя...')



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
