import datetime
from time import strptime, strftime


def sum_timestamps(time_lst):
    sumy = datetime.timedelta()
    for i in time_lst:
        (m, s) = i.split(':')
        d = datetime.timedelta(minutes=int(m), seconds=int(s))
        sumy += d
        frey = strptime(str(sumy), '%H:%M:%S')
    return strftime('%H:%M:%S', frey)
    # print(str(sumy))


print(sum_timestamps(['5:32', '4:48']))
print(sum_timestamps(['03:10', '01:00']))
print(sum_timestamps(['2:01', '04:05']))
print(sum_timestamps(['15:32', '45:48']))
