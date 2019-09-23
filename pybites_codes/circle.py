from math import pi

# python morsel challenge


class Circle(object):

    def __init__(self, radius=1):
        self.radius = radius
        #self.diameter = self.radius * 2
        #self.area = radius ** 2 * pi

    def __repr__(self):
        return f'Circle({self.radius})'

    @property
    def area(self):
        return pi * self.radius ** 2
# bonus 2

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self._radius = diameter/2


# bonus three
    @property
    def radius(self):
        return self.radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError('radius can not be negative')
        self._radius = radius


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
