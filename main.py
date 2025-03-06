import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import API_KEY  # Подключаем API-ключ из config.py

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_KEY)
dp = Dispatcher()

# Клавиатура с вариантами выбора
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Зарплата")],
        [KeyboardButton(text="Пенсия")],
        [KeyboardButton(text="Кредитная карта")]
    ],
    resize_keyboard=True
)

# Обработчик команды /start
@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}!\nКакой продукт вас интересует?",
        reply_markup=keyboard
    )

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())