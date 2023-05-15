from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from tgbot.services.date import isBirthDay, getRelative, getToday, getDate
from tgbot.services.notifier import sendNotify
from tgbot.services.db import Database
db = Database()

scheduler = AsyncIOScheduler()


def jobSchedule(dp):
    scheduler.add_job(checkBirthday, args=[dp], trigger=CronTrigger(hour=5))
    # scheduler.add_job(test, trigger="interval", seconds=5)


def scheduleStart():
    scheduler.start()


async def test():
    print("Hello")


async def checkBirthday(dp):
    users = db.getUser()
    for user in users:
        day = user[4]
        month = user[5]
        year = user[6]

        isBirth = isBirthDay(day, month, year)
        relative = getRelative(getToday(), getDate(day, month, year))

        if isBirth:
            await sendNotify(user, relative, dp)
