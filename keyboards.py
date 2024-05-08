from aiogram import types


button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/игра')
button3 = types.KeyboardButton(text='/число')
button4 = types.KeyboardButton(text='/Лиса')
button5 = types.KeyboardButton(text='/ip')
button6 = types.KeyboardButton(text='/BTC')


keyboard1 = [
    [button1, button2, button3],
    [button4, button5, button6]
]


keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)