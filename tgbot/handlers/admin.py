from aiogram import Dispatcher
from aiogram.types import Message, ContentTypes
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.dispatcher import FSMContext

from tgbot.texts import user
from tgbot.texts import admin
import tgbot.keyboards as keyboard

from tgbot.services.db import Database
from tgbot.services.states import AddCategory, AddUser

db = Database()


async def admin_start(message: Message):
    await message.reply(
        admin.start,
        reply_markup=keyboard.inline.admin.admin_panel
    )

    await message.answer(
        user.start,
        reply_markup=keyboard.inline.user.users_list
    )


async def deleteCategory(msg: Message):
    categoryID = str(msg.text).replace("/delCategory_", "")

    db.deleteCategory(categoryID)
    await msg.reply(
        admin.category.deleted
    )


async def descriptionForCategory(msg: Message, state: FSMContext):
    await state.update_data(description=str(msg.text))

    await msg.answer(
        admin.category.groupIDSend
    )

    await AddCategory.groupID.set()


async def groupIDForCategory(msg: Message, state: FSMContext):
    data = await state.get_data()

    db.addCategory(data.get("description"), msg.text)

    await msg.answer(
        admin.category.added
    )

    await state.finish()


async def addUserGetFirstName(msg: Message, state: FSMContext):
    firstName = str(msg.text)
    await state.update_data(firstName=firstName)

    await msg.answer(
        admin.newUser.lastName
    )

    await AddUser.lastName.set()


async def addUserGetLastName(msg: Message, state: FSMContext):
    lastName = str(msg.text)
    await state.update_data(lastName=lastName)

    await msg.answer(
        admin.newUser.fatherhood
    )

    await AddUser.fatherhood.set()


async def addUserGetFatherhood(msg: Message, state: FSMContext):
    fatherhood = str(msg.text)
    await state.update_data(fatherhood=fatherhood)

    await msg.answer(
        admin.newUser.dateOfBirth
    )

    await AddUser.dateOfBirth.set()


async def addUserGetDate(msg: Message, state: FSMContext):
    date = str(msg.text).split("/")
    day = date[0]; month = date[1]; year = date[2]

    await state.update_data(
        day=day,
        month=month,
        year=year
    )

    await msg.answer(
        admin.newUser.category,
        reply_markup=keyboard.inline.admin.category().addUser()
    )
    await AddUser.categoryType.set()


async def getIDOfGroup(msg: Message):
    await msg.answer(
        msg.chat.id
    )


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(deleteCategory, Text(startswith="/delCategory_"), state="*", is_admin=True)
    dp.register_message_handler(descriptionForCategory, content_types=ContentTypes.TEXT, state=AddCategory.description, is_admin=True)
    dp.register_message_handler(groupIDForCategory, content_types=ContentTypes.TEXT, state=AddCategory.groupID, is_admin=True)
    dp.register_message_handler(getIDOfGroup, commands='id', state="*", is_admin=True)

    dp.register_message_handler(addUserGetFirstName, content_types=ContentTypes.TEXT, state=AddUser.firstName, is_admin=True)
    dp.register_message_handler(addUserGetLastName, content_types=ContentTypes.TEXT, state=AddUser.lastName, is_admin=True)
    dp.register_message_handler(addUserGetFatherhood, content_types=ContentTypes.TEXT, state=AddUser.fatherhood, is_admin=True)
    dp.register_message_handler(addUserGetDate, content_types=ContentTypes.TEXT, state=AddUser.dateOfBirth, is_admin=True)
