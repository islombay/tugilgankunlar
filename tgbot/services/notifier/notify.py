from aiogram import Dispatcher

from tgbot.texts import user as userText
from tgbot.services.db import Database
db = Database()


async def sendNotify(user, relative, dp: Dispatcher):
    firstName = user[1]
    lastName = user[2]
    category = user[5]

    newAge = relative.years
    groupID = (db.getCategory(category))[2]
    groupID = groupID.split(",")

    for id in groupID:
        await dp.bot.send_message(
            chat_id=id,
            text=userText.birthdayText.format(
                lastName, firstName,
                newAge
            )
        )
