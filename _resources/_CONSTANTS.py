# /_resources/CONSTANT.py

from datetime import datetime

# Date minimum pour que le calcul fonctionne
MIN_DATE = datetime.strptime("1/11/2018", '%d/%m/%Y').date()

# Value has to add according to month( 0 = January, 11 = December)
MONTH_VALUE = [
    0,
    3,
    3,
    6,
    1,
    4,
    6,
    2,
    5,
    0,
    3,
    5
]

# Value has to add according to the century
CENTURY_VALUE = {
    16: 6,
    17: 4,
    18: 2,
    19: 0,
    20: 6,
    21: 4
}

# Value to define the day of the date
DAY_VALUE = {
    0: "Dimanche",
    1: "Lundi",
    2: "Mardi",
    3: "Mercredi",
    4: "Jeudi",
    5: "Vendredi",
    6: "Samedi"
}
