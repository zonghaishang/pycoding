from typing import Protocol, runtime_checkable, TypeVar
from abc import abstractmethod

T_co = TypeVar('T_co', covariant=True)


@runtime_checkable
class SupportsAbs(Protocol[T_co]):
    __slots__ = ()

    @abstractmethod
    def __abs__(self) -> T_co:
        pass
