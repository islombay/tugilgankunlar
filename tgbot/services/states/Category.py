from aiogram.dispatcher.filters.state import StatesGroup, State


class AddCategory(StatesGroup):
    description = State()
    groupID = State()