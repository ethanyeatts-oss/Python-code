import math


class Point:
    """creates class to contain points"""

    def __init__(self, x, y):
        """ initialize point  """
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def distance_to_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to(self, p2):
        return math.sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)

    def copy(self):
        return Point(self.x, self.y)


class Line:
    """a class to contain a line segment"""

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return str(self.start) + " to " + str(self.end)

    def length(self):
        return self.start.distance_to(self.end)

    def slope(self):
        if self.start.x == self.end.x:
            return "The slope is undefined"
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)

    def crosses_x(self):
        return (self.start.y < 0 and self.end.y > 0) or \
               (self.start.y > 0 and self.end.y < 0)

    def crosses_y(self):
        return (self.start.x < 0 and self.end.x > 0) or \
               (self.start.x > 0 and self.end.x < 0)


p1 = Point(1, 2)
p2 = Point(3, 6)
line = Line(p1, p2)
print(line)
print(line.length())
print(line.slope())
print(line.crosses_x())
print()

p1 = Point(1, 2)
p2 = Point(1, 6)
line2 = Line(p1, p2)
print(line2.slope())