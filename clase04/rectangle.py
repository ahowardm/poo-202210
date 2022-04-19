from figure import Figure

class Rectangle(Figure):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * self.height + 2 * self.width

    def get_type(self):
        return 'Rectangulo'