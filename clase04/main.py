from circle import Circle
from rectangle import Rectangle
from triangle import Triangle

my_circle = Circle(3)
my_circle.greet()

my_rectangle = Rectangle(5, 4)
my_rectangle.greet()

my_triangle = Triangle(2, 4)
my_triangle.greet()
print(my_triangle.perimeter())
