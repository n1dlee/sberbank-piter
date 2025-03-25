from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
import logging
from config import API_KEY
from credit_card import credit_card_router
from protection import protection_router
from health import health_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=API_KEY)
dp = Dispatcher()

dp.include_router(credit_card_router)
dp.include_router(protection_router)
dp.include_router(health_router)

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Кредитная карта")],
        [KeyboardButton(text="Защита на любой случай")],
        [KeyboardButton(text="Сберздоровье")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}!\nКакой продукт вас интересует?",
        reply_markup=main_keyboard
    )

async def main():
    logger.info("Бот запущен!")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Ошибка в работе бота: {e}")
    finally:
        await bot.session.close()
        logger.info("Бот остановлен.")

if __name__ == "__main__":
    asyncio.run(main())