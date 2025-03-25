from aiogram import Router, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

health_router = Router()

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
health_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Вариант 1 (Здоровье)")],
        [KeyboardButton(text="Вариант 2 (Здоровье)")]
    ],
    resize_keyboard=True
)

# Клавиатуры для ответов
yes_no_keyboards = {
    "Вариант 1 (Здоровье)": ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Да, очень часто (Здоровье)")], [KeyboardButton(text="Нет, не хожу (Здоровье)")]],
        resize_keyboard=True
    ),
    "Вариант 2 (Здоровье)": ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Да, сталкивался (Здоровье)")], [KeyboardButton(text="Нет, не сталкивался (Здоровье)")]],
        resize_keyboard=True
    ),
}

# Кнопка "Мне это интересно!"
interest_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Мне это интересно!")]],
    resize_keyboard=True
)

@health_router.message(lambda message: message.text == "Сберздоровье")
async def health_info(message: types.Message):
    await message.answer(
        "Сформируйте потребность клиента данными вопросами:\n"
        "1) У вас есть дети? Как часто обращаетесь к педиатру по вопросам их здоровья?\n"
        "2) Были ли у вас ситуации, когда не было возможности очно прийти на прием, "
        "потому что срочные вопросы со здоровьем возникали ночью, на даче или за границей?",
        reply_markup=health_keyboard
    )

@health_router.message(lambda message: message.text in yes_no_keyboards.keys())
async def handle_variant(message: types.Message):
    await message.answer("Выберите ответ:", reply_markup=yes_no_keyboards[message.text])

@health_router.message(lambda message: message.text.endswith("(Здоровье)") and "Да" in message.text)
async def handle_variant_yes(message: types.Message):
    answers = {
        "Да, очень часто (Здоровье)": "Семья возвращалась на машине из отпуска, у ребенка проявился ротавирус. "
                                       "Они обратились за онлайн-консультацией, купили лекарства и начали лечение.",
        "Да, сталкивался (Здоровье)": "Мужчина с высокой температурой вызвал врача. "
                                       "ОРВИ не подтвердилось, но онлайн-врач заметил сыпь – оказалась ветрянка. "
                                       "Он получил точный диагноз и рекомендации.",
    }
    await message.answer(answers[message.text], reply_markup=interest_keyboard)

@health_router.message(lambda message: message.text.endswith("(Здоровье)") and "Нет" in message.text)
async def handle_variant_no(message: types.Message):
    await health_info(message)

@health_router.message(lambda message: message.text == "Мне это интересно!")
async def restart(message: types.Message):
    await message.answer("Какой продукт вас интересует?", reply_markup=main_keyboard)
