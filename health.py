from aiogram import Router, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

health_router = Router()

# Клавиатура для вопросов
health_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Вариант 1")],
        [KeyboardButton(text="Вариант 2")]
    ],
    resize_keyboard=True
)

# Клавиатура для выбора ответа
yes_no_keyboard_1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да, очень часто")],
        [KeyboardButton(text="Нет, не хожу")]
    ],
    resize_keyboard=True
)

yes_no_keyboard_2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да, сталкивался")],
        [KeyboardButton(text="Нет, не сталкивался")]
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

# Обработчик выбора "Сберздоровье"
@health_router.message(lambda message: message.text == "Сберздоровье")
async def health_info(message: types.Message):
    await message.answer(
        "Сформируйте потребность клиента данными вопросами:\n"
        "1) У вас есть дети? Как часто обращаетесь к педиатру по вопросам их здоровья?\n"
        "2) Были ли у вас ситуации, когда не было возможности очно прийти на прием, "
        "потому что срочные вопросы со здоровьем возникали ночью, на даче или за границей?",
        reply_markup=health_keyboard
    )

@health_router.message(lambda message: message.text == "Вариант 1")
async def option_1(message: types.Message):
    await message.answer("У вас есть дети? Как часто обращаетесь к педиатру по вопросам их здоровья?", reply_markup=yes_no_keyboard_1)

@health_router.message(lambda message: message.text == "Вариант 2")
async def option_2(message: types.Message):
    await message.answer("Были ли у вас ситуации, когда не было возможности очно прийти на прием, "
                         "потому что срочные вопросы со здоровьем возникали ночью, на даче или за границей?",
                         reply_markup=yes_no_keyboard_2)

# Обработчики ответов на вопросы
@health_router.message(lambda message: message.text == "Да, очень часто")
async def answer_1_yes(message: types.Message):
    await message.answer(
        "Мои знакомые (семья с ребенком) возвращались на автомобиле из отпуска. В дороге у ребенка проявился ротавирус. "
        "Потребовалась срочная консультация врача. Обратились за онлайн-консультацией к педиатру и получили детальную консультацию. "
        "По дороге заехали в аптеку и купили препараты, назначенные врачом. И сразу приступили к лечению.",
        reply_markup=interest_keyboard
    )

@health_router.message(lambda message: message.text == "Да, сталкивался")
async def answer_2_yes(message: types.Message):
    await message.answer(
        "Мужчина с высокой температурой вызвал врача на дом. Врач поставил ОРВИ и прописал лечение. "
        "Тест на коронавирус был отрицательным. Лечение не помогало, температура держалась. "
        "После чего мужчина решил обратиться за онлайн-консультацией, и по видеосвязи врач обратил внимание на высыпание на лице. "
        "После нескольких вопросов и сбора анамнеза была определена ветрянка и даны рекомендации к лечению.",
        reply_markup=interest_keyboard
    )

# Обработчик кнопки "Мне это интересно!"
@health_router.message(lambda message: message.text == "Мне это интересно!")
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
