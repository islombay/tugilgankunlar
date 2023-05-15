from aiogram.dispatcher.filters.state import State, StatesGroup

class AddUser(StatesGroup):
    firstName = State()
    lastName = State()
    fatherhood = State()
    dateOfBirth = State()
    categoryType = State()