from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

kb_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Получить аудиодорожку!')
        ],
    ], resize_keyboard=True, one_time_keyboard=True
)