# /_resources/_FUNCTIONS.py

def valueLeapYear(year, month):
    """
    :param year: the year of the date to test
    :param month: the month of the date to test
    :return: -1 if the year of date is a leap year and if the month is January of February
    """
    if((year%4 == 0 and year%100 !=0 or year%400 == 0) and month == (1 or 2)):
        return -1
    return 0

