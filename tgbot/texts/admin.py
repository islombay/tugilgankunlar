from typing import List
from tgbot.services.db import Database

db = Database()


class admin:
    start = "Admin panel"

    class category:
        no = "Category mavjud emas"
        deleted = "Category o'chirilib yuborildi"

        title = "Category'ni description ni yuboring"
        groupIDSend = "Category'ni group id'sini yuboring"
        added = "Category qo'shildi"

    class newUser:
        firstName = "User'ning ismini yuboring"
        lastName = "User'ning familiyasini yuboring"
        fatherhood = "User'ning otasining ismi"
        dateOfBirth = "User'ning tug'ilgan sanasi\nMisol: kun/oy/yil - 01/05/2021"
        category = "User'ning category'si"

        successful = "User qo'shildi ✅"

    class showCategsTitle:
        def __str__(self):
            self.text = ""

            categoriesList = db.getCategory()

            if bool(len(categoriesList)):
                for e in categoriesList:
                    self.text += f"ID: {e[0]}\nDescription: {e[1]}\nDelete: /delCategory_{e[0]}\n\n"

            else: self.text = admin.category.no

            return f"<b>📎 Categories List</b>:\n{self.text}"
