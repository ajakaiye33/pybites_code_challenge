# morsel of python challenge
"""
The Point class must accept 3 values on initialization (x, y, and z)
and have x, y, and z attributes. It must also have a helpful string representation.
Additionally, point objects should be comparable to each other
(two points are equal if their coordinates are the same and not equal otherwise).
"""


class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


coordinate = Point(1, 2, 3)
corddy = Point(1, 2, 3)
print(coordinate == corddy)
