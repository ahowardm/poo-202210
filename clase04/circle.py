from figure import Figure
from math import pi

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

    def get_type(self):
        return 'Circulo'
