from collections import namedtuple

Coordinate = namedtuple('Coordinate', ['lat', 'lon'])
print("issubclass(Coordinate, tuple)", issubclass(Coordinate, tuple))

moscow = Coordinate(1, 2)
print(moscow)

print(moscow == Coordinate(1, 2))
