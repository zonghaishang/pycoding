import math
from typing import NamedTuple, SupportsAbs


class Vector2d(NamedTuple):
    x: float
    y: float

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)


class Vector2d_v1(NamedTuple):
    x: float
    y: float

    def __abs__(self) -> int:
        f = math.hypot(self.x, self.y)
        return int(f)


def is_unit(v: SupportsAbs[float]) -> bool:
    return math.isclose(abs(v), 1.0)


print(issubclass(Vector2d, SupportsAbs))
print(issubclass(Vector2d_v1, SupportsAbs))
