class Month():
    def __init__(self, year, month):
        self.year = year
        self.month = month
        turny = '{}-{}'.format(year, month)
        print(turny)


dec99 = Month(1999, 12)
print(dec99)
