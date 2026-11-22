class Temperature:
    def __init__(self):
        self.celsius = 0

    def set_celsius(self, temperature):
        self.celsius = temperature

    def set_fahrenheit(self, temperature):
        self.celsius = (temperature - 32) * 5 / 9

    def set_kelvin(self, temperature):
        self.celsius = temperature - 273.15

    def as_celsius(self):
        return self.celsius

    def as_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    def as_kelvin(self):
        return self.celsius + 273.15


t = Temperature()
t.set_fahrenheit(75)
print("Temperature in Celsius:", round(t.as_celsius(), 2))
print("Temperature in Kelvin:", round(t.as_kelvin(), 2))
print("Temperature in Fahrenheit:", round(t.as_fahrenheit(), 2))
print()

t.set_celsius(2.5)
print("Temperature in Celsius:", round(t.as_celsius(), 2))
print("Temperature in Kelvin:", round(t.as_kelvin(), 2))
print("Temperature in Fahrenheit:", round(t.as_fahrenheit(), 2))

