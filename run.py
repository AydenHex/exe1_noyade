# /run.py

from _resources import _CONSTANTS, _FUNCTIONS
from datetime import datetime

dateValide = False
date = ""
# While date < november 1st 1582 and date in the right format
while not dateValide:
    try:
        # try to get the date to test
        date = datetime.strptime(input("Veuillez entrer une date sous format jj/mm/yyyy"), "%d/%m/%Y")
    except ValueError:
        print("Mauvais format !")
    except:
        print("Erreur")
    else:
        # if date is after november 1st 1582
        if date > datetime.strptime("01/11/1582", "%d/%m/%Y"):
            dateValide = True
        else:
            print("Veuillez entrer une date supérieur au 1er novembre 1582")

# initialization of the variable for the day calculation
total = 0

# variable for the day, month and year
day = date.day
month = date.month
year = date.year

# split of the date (19|84)
last_number_year = int(str(year)[-2:])
century = int(str(year)[:-2])

# day calculation
total = (last_number_year + last_number_year // 4 + day + _CONSTANTS.MONTH_VALUE[month - 1] + _FUNCTIONS.valueLeapYear(
    year, month) + _CONSTANTS.CENTURY_VALUE[century]) % 7

# print of the result
print("Le " + str(date.date()) + ", nous étions un " + _CONSTANTS.DAY_VALUE[total])
