from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.texts import user
import tgbot.keyboards as keyboard


async def user_start(message: Message):
    await message.answer(
        user.start,
        reply_markup=keyboard.inline.user.users_list
    )


async def add_user(msg: Message):
    pass


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(add_user, commands=['add_user'], state="*")
