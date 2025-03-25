from aiogram import Router, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

protection_router = Router()

# Главная клавиатура
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Кредитная карта")],
        [KeyboardButton(text="Защита на любой случай")],
        [KeyboardButton(text="Сберздоровье")]
    ],
    resize_keyboard=True
)

# Клавиатура с вариантами
protection_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Вариант 1 (Защита)")],
        [KeyboardButton(text="Вариант 2 (Защита)")],
        [KeyboardButton(text="Вариант 3 (Защита)")]
    ],
    resize_keyboard=True
)

# Клавиатуры для ответов
yes_no_keyboards = {
    "Вариант 1 (Защита)": ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Да, важно (Защита)")], [KeyboardButton(text="Нет, не очень (Защита)")]],
        resize_keyboard=True
    ),
    "Вариант 2 (Защита)": ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Да, знаю (Защита)")], [KeyboardButton(text="Нет, не знал(а) (Защита)")]],
        resize_keyboard=True
    ),
    "Вариант 3 (Защита)": ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Да, давайте (Защита)")], [KeyboardButton(text="Нет, не интересно (Защита)")]],
        resize_keyboard=True
    ),
}

# Кнопка "Мне это интересно!"
interest_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Мне это интересно!")]],
    resize_keyboard=True
)

@protection_router.message(lambda message: message.text == "Защита на любой случай")
async def protection_info(message: types.Message):
    await message.answer(
        "Сформируйте потребность клиента данными вопросами:\n"
        "1) Вам важно сохранить денежные средства на своей карте?\n"
        "2) Знаете, что сейчас увеличилось количество звонков от мошенников в 11 раз?\n"
        "3) Рассказать, как защитить себя от оформления на вас кредита 3-ми лицами?",
        reply_markup=protection_keyboard
    )

@protection_router.message(lambda message: message.text in yes_no_keyboards.keys())
async def handle_variant(message: types.Message):
    await message.answer("Выберите ответ:", reply_markup=yes_no_keyboards[message.text])

@protection_router.message(lambda message: message.text.endswith("(Защита)") and "Да" in message.text)
async def handle_variant_yes(message: types.Message):
    answers = {
        "Да, важно (Защита)": "К нам недавно обратился клиент, не знал, что карту потерял. "
                               "Злоумышленник нашел её и рассчитывался 10 дней без пин-кода. "
                               "Чтобы такого не случилось, нужно поставить защиту на любой случай.",
        "Да, знаю (Защита)": "Когда звонят мошенники и представляются службой безопасности, "
                             "многие клиенты идут на это и теряют деньги. Чтобы не попасть в такую ситуацию, "
                             "нужна защита на любой случай.",
        "Да, давайте (Защита)": "Коллеги по работе клиента сделали копию его паспорта и оформили на него кредит. "
                                 "Если бы у него была защита, он бы смог компенсировать судебные издержки.",
    }
    await message.answer(answers[message.text], reply_markup=interest_keyboard)

@protection_router.message(lambda message: message.text.endswith("(Защита)") and "Нет" in message.text)
async def handle_variant_no(message: types.Message):
    await protection_info(message)

@protection_router.message(lambda message: message.text == "Мне это интересно!")
async def restart(message: types.Message):
    await message.answer("Какой продукт вас интересует?", reply_markup=main_keyboard)
