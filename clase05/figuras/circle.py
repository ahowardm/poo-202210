from figure import Figure
from math import pi

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def validate_radius(value):
        if not isinstance(value, int):
            raise TypeError('El radio debe ser un número')
        if (value < 0):
            raise ValueError(f'El radio {value} no es válido. Debe ser mayor que 0')

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.validate_radius(value)
        self.__radius = value

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

    def get_type(self):
        return 'Circulo'
