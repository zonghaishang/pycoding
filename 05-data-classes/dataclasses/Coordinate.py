import dataclasses
from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

    def __str__(self) -> str:
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns} {abs(self.lon):.1f}°{we}'


print(issubclass(Coordinate, tuple))
print(Coordinate(1, 2))

print(dataclasses.asdict(Coordinate(2, 3)))

fields = [(f.name, f.default) for f in dataclasses.fields(Coordinate(1, 2))]
print(fields)

# dataclasses.make_dataclass()
