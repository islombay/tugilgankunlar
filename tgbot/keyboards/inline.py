from dataclasses import dataclass

from aiogram.types import InlineKeyboardButton as btn, InlineKeyboardMarkup

from tgbot.services.db import Database
db = Database()


@dataclass
class user:
    users_list = InlineKeyboardMarkup().add(
        btn("🗂 Qarindoshlar", callback_data="relatives")
    ).add(
        btn("➕ Profil qo'shish", callback_data="addProfile")
    )


@dataclass
class admin:
    admin_panel = InlineKeyboardMarkup().add(
        btn("🗂 Barcha user'lar", callback_data="allUsers")
    ).add(
        btn("➕ Yangi qo'shish", callback_data="addNewUser")
    ).add(
        btn("📎 Categories", callback_data="showCategs")
    )

    addCategory = InlineKeyboardMarkup().add(
        btn("➕ Category qo'shish", callback_data="addCategory")
    )

    class category:
        def addUser(self):
            k = InlineKeyboardMarkup()

            categoriesList = db.getCategory()
            for c in categoriesList:
                k.add(
                    btn(f"Category {c[0]}", callback_data=f"category_{c[0]}")
                )

            return k


@dataclass
class inline:
    user: user = user
    admin: admin = admin
