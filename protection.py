from aiogram import Router, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

protection_router = Router()

# Клавиатура для вопросов
protection_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Вариант 1")],
        [KeyboardButton(text="Вариант 2")],
        [KeyboardButton(text="Вариант 3")]
    ],
    resize_keyboard=True
)

# Клавиатура для выбора ответа
yes_no_keyboard_1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да, важно")],
        [KeyboardButton(text="Нет, не очень")]
    ],
    resize_keyboard=True
)

yes_no_keyboard_2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да, знаю")],
        [KeyboardButton(text="Нет, не знал(а)")]
    ],
    resize_keyboard=True
)

yes_no_keyboard_3 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да, давайте")],
        [KeyboardButton(text="Нет, не интересно")]
    ],
    resize_keyboard=True
)

# Клавиатура "Мне это интересно!"
interest_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Мне это интересно!")]
    ],
    resize_keyboard=True
)

# Обработчик выбора "Защита на любой случай"
@protection_router.message(lambda message: message.text == "Защита на любой случай")
async def protection_info(message: types.Message):
    await message.answer(
        "Сформируйте потребность клиента данными вопросами:\n"
        "1) Вам важно сохранить денежные средства на своей карте?\n"
        "2) Знаете, что сейчас увеличилось количество звонков от мошенников в 11 раз?\n"
        "3) Рассказать, как защитить себя от оформления на вас кредита 3-ми лицами?",
        reply_markup=protection_keyboard
    )

@protection_router.message(lambda message: message.text == "Вариант 1")
async def option_1(message: types.Message):
    await message.answer("Вам важно сохранить денежные средства на своей карте?", reply_markup=yes_no_keyboard_1)

@protection_router.message(lambda message: message.text == "Вариант 2")
async def option_2(message: types.Message):
    await message.answer("Знаете, что сейчас увеличилось количество звонков от мошенников в 11 раз?", reply_markup=yes_no_keyboard_2)

@protection_router.message(lambda message: message.text == "Вариант 3")
async def option_3(message: types.Message):
    await message.answer("Рассказать, как защитить себя от оформления на вас кредита 3-ми лицами?", reply_markup=yes_no_keyboard_3)

# Обработчики ответов на вопросы
@protection_router.message(lambda message: message.text == "Да, важно")
async def answer_1_yes(message: types.Message):
    await message.answer(
        "К нам недавно обратился клиент, не знал, что карту потерял, был в отпуске, связи не было. "
        "Злоумышленник нашёл карту и рассчитывался ей в течение 10 дней на суммы до 1000 руб без ввода пин-кода. "
        "Для защиты денежных средств необходимо поставить защиту на любой случай.",
        reply_markup=interest_keyboard
    )

@protection_router.message(lambda message: message.text == "Да, знаю")
async def answer_2_yes(message: types.Message):
    await message.answer(
        "Когда клиентам звонят мошенники, представляясь сотрудниками полиции или службы безопасности банка, "
        "они убеждают провести операции с кодом из смс. Многие клиенты идут на это, переводят средства и теряют деньги. "
        "Чтобы этого не произошло, необходимо поставить защиту на любой случай.",
        reply_markup=interest_keyboard
    )

@protection_router.message(lambda message: message.text == "Да, давайте")
async def answer_3_yes(message: types.Message):
    await message.answer(
        "У нашего клиента произошла ситуация: коллеги по работе сделали копию его паспорта и оформили на него кредит. "
        "Если бы он предположил, что подобное может случиться, то оформил бы программу и смог компенсировать судебные издержки. "
        "Чтобы обезопасить себя, поставьте защиту на любой случай.",
        reply_markup=interest_keyboard
    )

# Обработчик кнопки "Мне это интересно!"
@protection_router.message(lambda message: message.text == "Мне это интересно!")
async def restart(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}!\nКакой продукт вас интересует?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Кредитная карта")],
                [KeyboardButton(text="Защита на любой случай")],
                [KeyboardButton(text="Сберздоровье")]
            ],
            resize_keyboard=True
        )
    )
