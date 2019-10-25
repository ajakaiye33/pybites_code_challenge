import itertools

from datetime import datetime
from datetime import timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    hubdred_days = datetime.timedelta(days=100)
    three_sixty = datetime(day=360)
    sey = three_sixty + PYBITES_BORN
    print(sey)


print(gen_special_pybites_dates())
