import functools
import operator
from typing import TypeVar, overload, Iterable

T = TypeVar('T')
S = TypeVar('S')


@overload
def mysum(iterable: Iterable[T]) -> T | int: ...


@overload
def mysum(iterable: Iterable[T], /, start: S) -> T | S: ...


@overload
def mysum(iterable: Iterable[T], /, start: S, limit: int) -> T | S: ...


def mysum(it, /, start=0, limit=0):
    _ = limit
    return functools.reduce(operator.add, it, start)


print(mysum(range(0, 10), start=0, limit=1))
