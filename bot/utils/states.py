from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    username = State()
    slot = State()
