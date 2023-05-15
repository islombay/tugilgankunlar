import datetime
from dateutil.relativedelta import relativedelta


def getToday():
    t = datetime.datetime.today()
    return datetime.datetime(year=t.year, month=t.month, day=t.day)


def getDate(day, month, year):
    return datetime.datetime(year=int(year), month=int(month), day=int(day))


def getRelative(today, birth=None):
    if not birth:
        birth = getToday()

    return relativedelta(today, birth)


def isBirthDay(day, month, year):
    birth = getDate(day, month, year)
    today = getToday()

    diff = getRelative(today, birth)

    dayDiff = diff.days
    monthDiff = diff.months
    yearDiff = diff.years

    if not bool(dayDiff) and not bool(monthDiff) and yearDiff:
        return True

    return False
