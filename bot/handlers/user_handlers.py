from aiogram import Router

from aiogram.types import Message
from aiogram import filters



user_router = Router()

ready_for_poll: bool = False

team: str
full_name: str


@user_router.message(filters.CommandStart())
async def start(message: Message) -> None:
    GREETING = """
<b>Привет!</b>

Я бот, который помогает собирать обратную связь в команде с использованием метода "Оценка 360"
"""
    await message.answer(text=GREETING, parse_mode='HTML')
    

@user_router.message(filters.Command("identify"))
async def identify(message: Message) -> None:
    global full_name, team
    full_name = await input_team(message)
    full_name = await input_full_name(message)

    TEXT = f"Вы в команде {team} и ваше имя {full_name}. Все верно?"
    await message.answer(text=TEXT)

    
async def input_team(message: Message) -> None:
    exists: bool = False
    await message.answer(text="Введите название команды")
    if exists:
        return "team"
    else:
        return "default_team"
    

async def input_full_name(message: Message) -> str:
    exists: bool = False
    await message.answer(text="Введите ваше ФИО")
    if exists:
        return "name"
    else:
        return "default_name"



