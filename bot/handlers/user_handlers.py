import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


from backend import sheets_functions 

from aiogram import Router, F

from aiogram.types import Message
from aiogram import filters
from bot.states import authorisation
from aiogram.fsm.context import FSMContext



user_router = Router()

team: str
team_id: int

full_name: str


@user_router.message(F.text == '/start')
async def start(message: Message, state: FSMContext) -> None:
    """Starts the bot and greets the user"""
    
    await state.set_state(authorisation.DEFAULT)
    GREETING = """<b>Привет!</b> 🫣\nЯ бот, который помогает собирать обратную связь в команде с использованием метода <b>"Оценка 360"</b>\n\nДля начала работы введите команду /identify"""
    await message.answer(text=GREETING, parse_mode='HTML')
    

@user_router.message(filters.Command("identify"))
async def identify(message: Message, state: FSMContext) -> None:
    """Starts the identification process"""
    
    await message.answer(text="Введите название вашей команды")
    # start team validation input dialog
    await state.set_state(authorisation.TEAM_DIALOG)


@user_router.message(authorisation.TEAM_DIALOG)
async def validate_team(message: Message, state: FSMContext):
    """Validates the team name and checks if it exists in the database"""
    
    global team, team_id
    user_input_team: str = message.text
    bot_response = await message.answer(text="...")

    # check if team exists in database
    id: int = sheets_functions.check_team(user_input_team)
    if not(id):
        await bot_response.edit_text(f"""Информация о команде <b>"{user_input_team}"</b> отсутствует ❌.\nПожалуйста, попробуйте еще раз""", parse_mode='HTML')
    else:
        team = user_input_team
        team_id = id
        await bot_response.edit_text(f"""Команда <b>"{team}"</b> найдена 🎉.\nВведите ваше ФИО""", parse_mode='HTML')
        # start member validation input dialog
        await state.set_state(authorisation.FULL_NAME_DIALOG)


@user_router.message(authorisation.FULL_NAME_DIALOG)        
async def validate_member(message: Message, state: FSMContext):
    """Validates the member name and checks if it exists in the database"""

     # !!!!! Not Finished yet !!!!!
   
    await message.answer(text="We are here in process_full_name")
    global full_name
    user_input_full_name = message.text
    # check if member exists in database
    exists: int = sheets_functions.check_member(user_input_full_name)
    
    # if not exists:
    #     await message.answer(f"""Информация о команде <b>"{user_input_full_name}"</b> отсутствует ❌.\nПожалуйста, попробуйте еще раз""", parse_mode='HTML')
    # else:
    #     full_name = user_input_full_name
    #     await message.answer(f"""Команда <b>"{team}"</b> найдена 🎉.\nВведите ваше ФИО""", parse_mode='HTML')


@user_router.message(authorisation.AUTH_COMPLETED)
async def input_full_name_new(message: Message,state:FSMContext) -> str:
    
    # !!!!! Not Finished yet !!!!!
    
    global team
    global full_name
    full_name = message.text
    await message.answer(f'Team: {team}, name: {full_name}')





