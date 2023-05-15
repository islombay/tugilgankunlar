import sqlite3
# import logging

from tgbot.config import load_config
config = load_config(".env")

# logger = logging.getLogger(__name__)
# logging.basicConfig(
#         level=logging.INFO,
#         format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
#     )


class DBLite:
    def __init__(self):
        self.path = config.db.path
        self.connect()

    def connect(self):
        self.con = sqlite3.connect(self.path)
        self.cur = self.con.cursor()
        # logger.info("Database connected")

        return self.con

    def commit(self):
        self.con.commit()

    def getCategory(self, id=None):
        self.connect()

        res = 0
        if id:
            self.cur.execute("SELECT * FROM Categories WHERE id = ?", (id,))
            res = self.cur.fetchone()
        else:
            self.cur.execute("SELECT * FROM 'Categories'")
            res = self.cur.fetchall()

        return res

    def addCategory(self, desc, groupID):
        self.connect()
        self.cur.execute("INSERT INTO Categories (description, group_id) VALUES (?, ?)", (desc, groupID))
        self.con.commit()

    def deleteCategory(self, categoryID):
        self.connect()
        self.cur.execute("DELETE FROM Categories WHERE id = ?", (categoryID, ))
        self.commit()

    def addUser(self, fName, lName, fhood, day, month, year, ctype):
        self.connect()
        self.cur.execute(
            "INSERT INTO Users (first_name, last_name, fatherhood, day, month, year, categoryID) VALUES(?, ?, ?, ?, ?, ?, ?)",
            (fName, lName, fhood, day, month, year, ctype)
        )
        self.commit()

    def getUser(self, id: int = None):
        self.connect()
        res = 0

        if id:
            self.cur.execute("SELECT * FROM Users WHERE id = ?", (id,))
            res = self.cur.fetchone()
        else:
            self.cur.execute("SELECT * FROM Users")
            res = self.cur.fetchall()

        return res


if __name__ == '__main__':
    dbl = DBLite()

    print(dbl.getCategories())
    # dbl.addCategory("some")