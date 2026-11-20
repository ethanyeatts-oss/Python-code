import math


class Circle:
    def __init__(self, x = 0, y = 0, radius = 1):
        self.radius = radius
        self.x = x
        self.y = y

    def area(self):
        return self.radius**2  * math.pi

    def circumference(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        return self.radius * 2


circle_list = []

for i in range (1, 6):
    newCircle = Circle(radius = i)
    circle_list.append(newCircle)

for c in circle_list:
    print(f"{c.area():1.2f}")


