from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from aiogram.dispatcher.dispatcher import FSMContext

from tgbot.texts import admin
import tgbot.keyboards as keyboard

from tgbot.services.states import AddCategory, AddUser
from tgbot.services.db import Database
db = Database()


async def showCategories(call: CallbackQuery):
    text = admin.showCategsTitle()

    await call.message.answer(
        str(text),
        reply_markup=keyboard.inline.admin.addCategory
    )


async def addCategory(call: CallbackQuery, state: FSMContext):
    await call.message.answer(
        admin.category.title
    )
    # await call.message.edit_reply_markup()

    await AddCategory.description.set()


async def addNewUser(call: CallbackQuery):
    await call.message.answer(
        admin.newUser.firstName
    )

    await AddUser.firstName.set()


async def addUserGetCategory(call: CallbackQuery, state: FSMContext):
    cType = str(call.data).replace("category_", "")

    data = await state.get_data()
    db.addUser(
        data.get("firstName"),
        data.get("lastName"),
        data.get("fatherhood"),
        data.get("day"),
        data.get("month"),
        data.get("year"),
        int(cType)
    )

    await call.message.answer(
        admin.newUser.successful
    )

    await state.finish()


def register_inline_admin(dp: Dispatcher):
    dp.register_callback_query_handler(showCategories, text="showCategs", state="*", is_admin=True)
    dp.register_callback_query_handler(addCategory, text="addCategory", state="*", is_admin=True)
    dp.register_callback_query_handler(addNewUser, text="addNewUser", state="*", is_admin=True)

    dp.register_callback_query_handler(addUserGetCategory, text_startswith="category_", state=AddUser.categoryType, is_admin=True)
