import datetime


def sum_timestamps(time_lst):
    sumy = datetime.timedelta()
    for i in time_lst:
        (m, s) = i.split(':')
        d = datetime.timedelta(minutes=int(m), seconds=int(s))
        sumy += d
    print(str(sumy[3:]))


print(sum_timestamps(['5:32', '4:48']))
