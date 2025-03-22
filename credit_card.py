from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главная клавиатура для выбора продукта
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Зарплата")],
        [KeyboardButton(text="Пенсия")],
        [KeyboardButton(text="Кредитная карта")]
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
variant_1_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да, бывало")],
        [KeyboardButton(text="Нет, не бывало")]
    ],
    resize_keyboard=True
)

variant_2_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да, сталкивался")],
        [KeyboardButton(text="Нет, не сталкивался")]
    ],
    resize_keyboard=True
)

variant_3_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да, часто")],
        [KeyboardButton(text="Нет, не часто")]
    ],
    resize_keyboard=True
)

# Кнопка "Мне это интересно!" для возврата в самое начало
interest_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Мне это интересно!")]
    ],
    resize_keyboard=True
)

async def credit_card_start(message: types.Message):
    """ Начальный этап вопросов. """
    await message.answer(
        "Сформируйте потребность клиента данными вопросами:\n\n"
        "1) Приходилось ли вам занимать деньги у родственников/друзей?\n"
        "2) Сталкивались ли вы с непредвиденными расходами?\n"
        "3) Часто ли вы путешествуете?\n\n"
        "Выберите вариант ниже:",
        reply_markup=question_keyboard
    )

async def handle_variant_1(message: types.Message):
    """ Обработка выбора Вариант 1. """
    await message.answer("Приходилось ли вам занимать деньги у родственников/друзей?", reply_markup=variant_1_keyboard)

async def handle_variant_2(message: types.Message):
    """ Обработка выбора Вариант 2. """
    await message.answer("Сталкивались ли вы с непредвиденными расходами?", reply_markup=variant_2_keyboard)

async def handle_variant_3(message: types.Message):
    """ Обработка выбора Вариант 3. """
    await message.answer("Часто ли вы путешествуете?", reply_markup=variant_3_keyboard)

async def handle_variant_1_yes(message: types.Message):
    """ Обработка ответа 'Да, бывало' для Варианта 1. """
    await message.answer(
        "У меня есть кредитная карта и в случае когда мне не хватило по какой-то причине пары тысяч до зарплаты, "
        "я могу не просить ни у кого в долг, воспользоваться КК, а затем в течение льготного периода погасить задолженность и не платить проценты.",
        reply_markup=interest_keyboard
    )

async def handle_variant_2_yes(message: types.Message):
    """ Обработка ответа 'Да, сталкивался' для Варианта 2. """
    await message.answer(
        "Не так давно мне пришлось обновить зимние ботинки, прошлые неожиданно порвались. Так как стало уже холодно, ждать было нельзя, "
        "плюс мне хотелось приобрести качественную вещь, чтобы ситуация с порванными ботинками не повторилась. "
        "Мне очень помогла КК, я купила ботинки, вернула деньги в течение льготного периода и платить % не пришлось.",
        reply_markup=interest_keyboard
    )

async def handle_variant_3_yes(message: types.Message):
    """ Обработка ответа 'Да, часто' для Варианта 3. """
    await message.answer(
        "С кредитной картой я могу себе позволить забронировать билеты и отель в путешествие в тот момент, когда подвернется выгодное предложение, "
        "а не когда будет накоплена определенная сумма. Бронируешь, а деньги возвращаешь в течение льготного периода, очень удобно!\n\n"
        "Также я беру КК и в сам отпуск, на случай непредвиденных ситуаций.",
        reply_markup=interest_keyboard
    )

async def handle_variant_no(message: types.Message):
    """ Если ответ 'Нет', возвращаем к выбору вопросов. """
    await credit_card_start(message)

async def handle_interest(message: types.Message):
    """ Если пользователь нажал 'Мне это интересно!', возвращаем его в самое начало. """
    await message.answer(
        f"Привет, {message.from_user.full_name}!\nКакой продукт вас интересует?",
        reply_markup=main_keyboard
    )

def register_credit_card_handlers(dp: Dispatcher):
    """ Регистрация обработчиков сообщений. """
    dp.message.register(credit_card_start, lambda message: message.text == "Кредитная карта")
    dp.message.register(handle_variant_1, lambda message: message.text == "Вариант 1")
    dp.message.register(handle_variant_2, lambda message: message.text == "Вариант 2")
    dp.message.register(handle_variant_3, lambda message: message.text == "Вариант 3")

    dp.message.register(handle_variant_1_yes, lambda message: message.text == "Да, бывало")
    dp.message.register(handle_variant_2_yes, lambda message: message.text == "Да, сталкивался")
    dp.message.register(handle_variant_3_yes, lambda message: message.text == "Да, часто")

    dp.message.register(handle_variant_no, lambda message: message.text in ["Нет, не бывало", "Нет, не сталкивался", "Нет, не часто"])
    dp.message.register(handle_interest, lambda message: message.text == "Мне это интересно!")
