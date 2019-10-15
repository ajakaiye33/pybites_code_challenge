import itertools

from datetime import datetime
from datetime import timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


# def gen_special_pybites_dates():
#     yield PYBITES_BORN + 360


hundred_days = datetime.timedelta(days=1)
print(hundred_days + PYBITES_BORN)
