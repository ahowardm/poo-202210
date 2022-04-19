from math import pi

def circle_area(radius):
    if not isinstance(radius, int):
        raise TypeError('El radio debe ser un número')
    if (radius < 0):
        raise ValueError(f'El radio {radius} no es válido. Debe ser mayor que 0')
    else:
        return pi * radius ** 2

try:
    print(circle_area(5))
    print(circle_area(-1))
    print(circle_area(0))
except ValueError as ex:
    print('Hubo un error de valor')
    print(ex)
except TypeError as te:
    print('Hubo un error de tipo')
    print(te)
