from random import randint
from circle import Circle

for _ in range(10):
    radius = randint(-5, 5)
    try:
        print(f'{radius}: {Circle(radius).area()}')
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(f'{radius}: {Circle(-radius).area()}')