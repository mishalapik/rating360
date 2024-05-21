from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup


class authorisation(StatesGroup):
    DEFAULT = State()
    FULL_NAME = State()
    TEAM = State()
    TESTS_ACCEPTED = State()
