from aiogram import Router, F
from aiogram.types import Message

router = Router()

faq_text = (
    "❓ Часто задаваемые вопросы:\n\n"
    "🔹 Сколько стоит создание бота?\n"
    "Цены начинаются от 100$ и зависят от функциональности.\n\n"
    "🔹 Сколько времени занимает разработка?\n"
    "Обычно от 3 до 10 дней в зависимости от проекта.\n\n"
    "🔹 Какие технологии вы используете?\n"
    "Python, aiogram, PostgreSQL, Redis и другие."
)

@router.message(F.text == "❓ Частые вопросы")
async def send_faq(message: Message):
    await message.answer(faq_text)
