from aiogram import types


button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/stop')
button3 = types.KeyboardButton(text='/info')
button4 = types.KeyboardButton(text='/user')
button5 = types.KeyboardButton(text='/id')
button6 = types.KeyboardButton(text='/joke')


keyboard1 = [
    [button1, button2, button3],
    [button4, button5, button6]
]


keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)