from math import pi

# python morsel challenge


class Circle(object):

    def __init__(self, radius=1):
        self.radius = radius
        #self.diameter = self.radius * 2
        #self.area = radius ** 2 * pi

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self._diameter = value

    @property
    def area(self):
        return self.radius ** 2 * pi

    @area.setter
    def area(self, value):
        self._area = abs(-value)
        raise ValueError('radius can not be negative')


c = Circle()
# print(c.radius)
# print(c.diameter)
# print(c.area)
#
# d = Circle()
# print(d.radius)
# print(d.diameter)

print(c.radius)
#c.radius = 3
# print(c.diameter)
print(c.diameter)
print(c.area)
