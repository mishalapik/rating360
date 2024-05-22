import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from bot.states import authorisation
from aiogram import Router, F
from aiogram.types import Message
from aiogram import filters
from aiogram.fsm.context import FSMContext

from backend import sheets_functions 
from backend.User import User
from backend.MemberInfo import MemberInfo



user_router = Router()


"""local database of users"""
users: set = {}


@user_router.message(F.text == '/users')
async def start(message: Message, state: FSMContext) -> None:   
    """Debug function, shows all sessions"""

    TEXT = f""
    if not users:
        TEXT = "No users yet"
    for chat_id in users:
        TEXT += f"Chat ID – {chat_id}:\n{users[chat_id]}\n\n"
    await message.answer(text=TEXT, parse_mode='HTML')


@user_router.message(F.text == '/start')
async def start(message: Message, state: FSMContext) -> None:
    """Starts the bot and greets the user"""
    
    await state.set_state(authorisation.DEFAULT)
    GREETING = """<b>Привет!</b> 🫣\nЯ бот, который помогает собирать обратную связь в команде с использованием метода <b>"Оценка 360"</b>\n\nДля начала работы введите команду /identify"""
    await message.answer(text=GREETING, parse_mode='HTML')

    chat_id: int = message.chat.id
    if chat_id not in users:
        users[chat_id] = User()


@user_router.message(filters.Command("identify"))
async def identify(message: Message, state: FSMContext) -> None:
    """Starts the identification process"""
    
    await message.answer(text="Введите название вашей команды")
    # start team validation input dialog
    await state.set_state(authorisation.TEAM_DIALOG)

    chat_id: int = message.chat.id
    if chat_id not in users:
        users[chat_id] = User()


@user_router.message(authorisation.TEAM_DIALOG)
async def validate_team(message: Message, state: FSMContext):
    """Validates the team name and checks if it exists in the database"""
    
    bot_response = await message.answer(text="...")
    user_input_team: str = message.text

    # check if team exists in database
    team_id, sheets__team_row = sheets_functions.check_team(user_input_team)
    if not team_id:
        await bot_response.edit_text(f"""Информация о команде <b>"{user_input_team}"</b> отсутствует ❌\nПожалуйста, попробуйте еще раз""", parse_mode='HTML')
    else:
        chat_id: int = message.chat.id

        users[chat_id].team = user_input_team
        users[chat_id].team_id = team_id
        users[chat_id].sheets__team_row = sheets__team_row
        
        await bot_response.edit_text(f"""Команда <b>"{user_input_team}"</b> найдена 🎉""", parse_mode='HTML')
        await bot_response.answer(f"""Введите ваше ФИО""", parse_mode='HTML')
        # start member validation input dialog
        await state.set_state(authorisation.FULL_NAME_DIALOG)


@user_router.message(authorisation.FULL_NAME_DIALOG)        
async def validate_member(message: Message, state: FSMContext):
    """Validates the member name and checks if it exists in the database"""

    # !!!!! Not Finished yet !!!!!

    # // await message.answer(text="We are here in process_full_name")
    user_input_full_name = message.text

    # check if member exists in database
    # // exists: int = sheets_functions.check_member(user_input_full_name)
    chat_id: int = message.chat.id
    users[chat_id].member_info.full_name = user_input_full_name

    # complete identification
    await state.set_state(authorisation.AUTH_COMPLETED)
    
    # // if not exists:
    # //     await message.answer(f"""Информация о команде <b>"{user_input_full_name}"</b> отсутствует ❌.\nПожалуйста, попробуйте еще раз""", parse_mode='HTML')
    # // else:
    # //     full_name = user_input_full_name
    # //     await message.answer(f"""Команда <b>"{team}"</b> найдена 🎉.\nВведите ваше ФИО""", parse_mode='HTML')


@user_router.message(authorisation.AUTH_COMPLETED)
async def input_full_name_new(message: Message, state: FSMContext) -> str:
    
    # !!!!! Not Finished yet !!!!!

    chat_id: int = message.chat.id
    await message.answer(f'Authorization completed!!!\nTeam: {users[chat_id].team}, full_name: {users[chat_id].member_info.full_name}')
