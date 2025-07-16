import typing
from typing import NamedTuple

Coordinates = NamedTuple('Coordinates', [('x', float), ('y', float)])

moscow = Coordinates(1.0, 2.0)
print(moscow)

print(moscow == Coordinates(1.0, 2.0))

print(typing.get_type_hints(Coordinates))