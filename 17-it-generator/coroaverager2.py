from collections.abc import Generator
from typing import Union, NamedTuple


class Result(NamedTuple):
    count: int
    average: float


class Sentinel:
    def __repr__(self):
        return f'<Sentinel>'


STOP = Sentinel()
SendType = Union[float, Sentinel]


def average2(verbose: bool = False) -> Generator[None, SendType, Result]:
    total = 0.0
    count = 0
    avg = 0.0
    while True:
        term = yield
        if verbose:
            print('received:', term)
        if isinstance(term, Sentinel):
            break
        total += term
        count = count + 1
        avg = total / count
    return Result(count, avg)


def compute():
    result = yield from average2(verbose=True)
    print('computed:', result)


c = compute()
for v in [None, 10, 20, 30, STOP]:
    try:
        c.send(v)
    except StopIteration as ex:
        print('value:', ex.value)

print('-' * 20)

g = average2()
next(g)

print(g.send(10.0))
print(g.send(30.0))
try:
    print(g.send(STOP))
except StopIteration as s:
    result = s.value

print(result)

# print(g.close())
