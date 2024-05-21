from aiogram import Router,F

from aiogram.types import Message
from aiogram import filters
from states import authorisation
from aiogram.fsm.context import FSMContext

user_router = Router()

ready_for_poll: bool = False

team: str
full_name: str


@user_router.message(F.text == '/start')
async def start(message: Message, state: FSMContext) -> None:
    await state.set_state(authorisation.DEFAULT)
    GREETING = """
<b>Привет!</b>

Я бот, который помогает собирать обратную связь в команде с использованием метода "Оценка 360"
"""
    await message.answer(text=GREETING, parse_mode='HTML')
    

@user_router.message(filters.Command("identify"))
async def identify(message: Message, state: FSMContext) -> None:
    await state.set_state(authorisation.TEAM)
    await input_team(message, state)
    await state.set_state(authorisation.FULL_NAME)


async def input_team(message: Message, state: FSMContext) -> str:
    exists: bool = True
    await message.answer(text="Введите название команды")

    if exists:
        await state.set_state(authorisation.FULL_NAME)
        return message.text
    else:
        pass
    
    
    
    
@user_router.message(authorisation.FULL_NAME)
async def input_full_name(message: Message,state:FSMContext) -> str:
    exists: bool = False
    await message.answer(text="Введите ваше ФИО")
    global team
    team = message.text
    # if exists:
    #     pass
    # else:
    #     pass
    await state.set_state(authorisation.TESTS_ACCEPTED) 
@user_router.message(authorisation.TESTS_ACCEPTED)
async def input_full_name(message: Message,state:FSMContext) -> str:
    global team
    global full_name
    full_name = message.text
    await message.answer(f'Team: {team}, name: {full_name}')





