class Meters:
    def __init__(self, distance):
        self.distance = distance

    def __str__(self):
        return str(self.distance)

    def as_feet(self):
        return self.distance * 3.280839895

    def as_km(self):
        return self.distance / 1000

    def as_miles(self):
        return self.distance * 0.000621371

    def as_inches(self):
        return self.distance * 39.37007874


m = Meters(1234.567)
print(m, "meters")
print(m.as_feet(), "feet")
print(m.as_inches(), "inches")
print(m.as_km(), "km")
print(m.as_miles(), "miles")

