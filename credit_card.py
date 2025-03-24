from aiogram import types, Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

credit_card_router = Router()  # Создаём Router

# Главная клавиатура для выбора продукта
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Кредитная карта")],
        [KeyboardButton(text="Защита на любой случай")],
        [KeyboardButton(text="Сберздоровье")]
    ],
    resize_keyboard=True
)

# Клавиатура для выбора вопроса
question_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Вариант 1")],
        [KeyboardButton(text="Вариант 2")],
        [KeyboardButton(text="Вариант 3")]
    ],
    resize_keyboard=True
)

# Клавиатуры для ответов на вопросы
variant_keyboards = {
    "Вариант 1": ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Да, бывало")], [KeyboardButton(text="Нет, не бывало")]],
        resize_keyboard=True,
    ),
    "Вариант 2": ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Да, сталкивался")], [KeyboardButton(text="Нет, не сталкивался")]],
        resize_keyboard=True,
    ),
    "Вариант 3": ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Да, часто")], [KeyboardButton(text="Нет, не часто")]],
        resize_keyboard=True,
    ),
}

# Кнопка "Мне это интересно!" для возврата в самое начало
interest_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Мне это интересно!")]],
    resize_keyboard=True,
)

async def credit_card_start(message: types.Message):
    await message.answer(
        "Сформируйте потребность клиента данными вопросами:\n\n"
        "1) Приходилось ли вам занимать деньги у родственников/друзей?\n"
        "2) Сталкивались ли вы с непредвиденными расходами?\n"
        "3) Часто ли вы путешествуете?\n\n"
        "Выберите вариант ниже:",
        reply_markup=question_keyboard
    )

async def handle_variant(message: types.Message):
    """ Обработка выбора варианта и отправка соответствующего вопроса. """
    text, keyboard = {
        "Вариант 1": ("Приходилось ли вам занимать деньги у родственников/друзей?", variant_keyboards["Вариант 1"]),
        "Вариант 2": ("Сталкивались ли вы с непредвиденными расходами?", variant_keyboards["Вариант 2"]),
        "Вариант 3": ("Часто ли вы путешествуете?", variant_keyboards["Вариант 3"]),
    }[message.text]
    
    await message.answer(text, reply_markup=keyboard)

async def handle_variant_yes(message: types.Message):
    """ Обработка положительных ответов. """
    answer_texts = {
        "Да, бывало": "У меня есть кредитная карта и в случае когда мне не хватило пары тысяч до зарплаты, "
                      "я могу воспользоваться КК, а затем в течение льготного периода погасить задолженность без процентов.",
        "Да, сталкивался": "Недавно мне пришлось обновить зимние ботинки. Мне помогла КК, я купила ботинки, "
                           "вернула деньги в течение льготного периода и платить % не пришлось.",
        "Да, часто": "С КК я могу бронировать билеты и отели, когда вижу выгодное предложение, "
                     "а не ждать, пока накоплю деньги. Также беру КК в отпуск на случай непредвиденных ситуаций.",
    }
    
    await message.answer(answer_texts[message.text], reply_markup=interest_keyboard)

async def handle_variant_no(message: types.Message):
    """ Если ответ 'Нет', возвращаем к выбору вопросов. """
    await credit_card_start(message)

async def handle_interest(message: types.Message):
    """ Если пользователь нажал 'Мне это интересно!', возвращаем его в начало. """
    await message.answer(f"Привет, {message.from_user.full_name}!\nКакой продукт вас интересует?", reply_markup=main_keyboard)

# Регистрируем обработчики в роутере
credit_card_router.message.register(credit_card_start, lambda message: message.text == "Кредитная карта")
credit_card_router.message.register(handle_variant, lambda message: message.text in variant_keyboards.keys())
credit_card_router.message.register(handle_variant_yes, lambda message: message.text in ["Да, бывало", "Да, сталкивался", "Да, часто"])
credit_card_router.message.register(handle_variant_no, lambda message: message.text in ["Нет, не бывало", "Нет, не сталкивался", "Нет, не часто"])
credit_card_router.message.register(handle_interest, lambda message: message.text == "Мне это интересно!")
