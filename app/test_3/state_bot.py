from aiogram.fsm.state import StatesGroup, State


class StateTask(StatesGroup):
    title = State()
    description = State()
