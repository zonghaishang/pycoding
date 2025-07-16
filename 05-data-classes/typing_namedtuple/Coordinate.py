import typing
from typing import NamedTuple


class Coordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns} {abs(self.lon):.1f}°{we}'


print(issubclass(Coordinate, tuple))
print(Coordinate(1, 2))

