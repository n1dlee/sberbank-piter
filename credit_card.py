from aiogram import Router, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

credit_card_router = Router()

# Главная клавиатура
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Кредитная карта")],
        [KeyboardButton(text="Защита на любой случай")],
        [KeyboardButton(text="Сберздоровье")]
    ],
    resize_keyboard=True
)

# Клавиатура для вопросов
question_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Вариант 1 (Кредитка)")],
        [KeyboardButton(text="Вариант 2 (Кредитка)")],
        [KeyboardButton(text="Вариант 3 (Кредитка)")]
    ],
    resize_keyboard=True
)

# Клавиатура для ответов
yes_no_keyboards = {
    "Вариант 1 (Кредитка)": ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Да, бывало (Кредитка)")], [KeyboardButton(text="Нет, не бывало (Кредитка)")]],
        resize_keyboard=True
    ),
    "Вариант 2 (Кредитка)": ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Да, сталкивался (Кредитка)")], [KeyboardButton(text="Нет, не сталкивался (Кредитка)")]],
        resize_keyboard=True
    ),
    "Вариант 3 (Кредитка)": ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Да, часто (Кредитка)")], [KeyboardButton(text="Нет, не часто (Кредитка)")]],
        resize_keyboard=True
    ),
}

# Кнопка "Мне это интересно!"
interest_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Мне это интересно!")]],
    resize_keyboard=True
)

@credit_card_router.message(lambda message: message.text == "Кредитная карта")
async def credit_card_start(message: types.Message):
    await message.answer(
        "Сформируйте потребность клиента данными вопросами:\n\n"
        "1) Приходилось ли вам занимать деньги у родственников/друзей?\n"
        "2) Сталкивались ли вы с непредвиденными расходами?\n"
        "3) Часто ли вы путешествуете?\n\n"
        "Выберите вариант ниже:",
        reply_markup=question_keyboard
    )

@credit_card_router.message(lambda message: message.text in yes_no_keyboards.keys())
async def handle_variant(message: types.Message):
    await message.answer("Выберите ответ:", reply_markup=yes_no_keyboards[message.text])

@credit_card_router.message(lambda message: message.text.endswith("(Кредитка)") and "Да" in message.text)
async def handle_variant_yes(message: types.Message):
    answers = {
        "Да, бывало (Кредитка)": "У меня есть кредитная карта и в случае когда мне не хватило пары тысяч до зарплаты, "
                                 "я могу воспользоваться КК, а затем в течение льготного периода погасить задолженность без процентов.",
        "Да, сталкивался (Кредитка)": "Недавно мне пришлось обновить зимние ботинки. Мне помогла КК, я купил ботинки, "
                                       "вернул деньги в течение льготного периода и платить % не пришлось.",
        "Да, часто (Кредитка)": "С КК я могу бронировать билеты и отели, когда вижу выгодное предложение, "
                                 "а не ждать, пока накоплю деньги. Также беру КК в отпуск на случай непредвиденных ситуаций.",
    }
    await message.answer(answers[message.text], reply_markup=interest_keyboard)

@credit_card_router.message(lambda message: message.text.endswith("(Кредитка)") and "Нет" in message.text)
async def handle_variant_no(message: types.Message):
    await credit_card_start(message)

@credit_card_router.message(lambda message: message.text == "Мне это интересно!")
async def restart(message: types.Message):
    await message.answer("Какой продукт вас интересует?", reply_markup=main_keyboard)
