from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup


class authorisation(StatesGroup):
    DEFAULT = State()
    FULL_NAME_DIALOG = State()
    TEAM_DIALOG = State()
    AUTH_COMPLETED = State()
