from figure import Figure

class Triangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

    def perimeter(self):
        return self.base * 3

    def get_type(self):
        return 'Triangulo'