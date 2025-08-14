from collections.abc import Callable
from typing import get_type_hints, Any, NoReturn


class Field:

    def __init__(self, name: str, constructor: Callable) -> None:
        if not callable(constructor) or constructor is type(None):
            raise TypeError(f'{name!r} type hint must be callable')
        self.name = name
        self.storage_name = '_' + name
        self.constructor = constructor

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value) -> None:
        if value is ...:
            value = self.constructor()
        else:
            try:
                value = self.constructor(value)
            except (TypeError, ValueError) as e:
                type_name = self.constructor.__name__
                msg = f'{value!r} is not compatible with {self.name}: {type_name}'
                raise TypeError(msg) from e
        setattr(instance, self.storage_name, value)


class CheckedMeta(type):
    def __new__(mcs, cls_name, bases, cls_dict):
        if '__slots__' not in cls_dict:
            slots = []
            type_hints = cls_dict.get('__annotations__', {})
            for name, constructor in type_hints.items():
                field = Field(name, constructor)
                cls_dict[name] = field
                slots.append(field.storage_name)

            cls_dict['__slots__'] = slots

        return super().__new__(mcs, cls_name, bases, cls_dict)


class Checked(metaclass=CheckedMeta):
    __slots__ = ()

    @classmethod
    def _fields(cls) -> dict[str, type]:
        return get_type_hints(cls)

    def __init__(self, **kwargs: Any) -> None:
        for name in self._fields():
            value = kwargs.pop(name, ...)
            setattr(self, name, value)
        if kwargs:
            self.__flag_unknown_attrs(*kwargs)

    def __flag_unknown_attrs(self, *names: str) -> NoReturn:
        plural = 's' if len(names) > 1 else ''
        extra = ', '.join(f'{name!r}' for name in names)
        cls = repr(self)
        raise AttributeError(f'{cls} object has no attribute{plural} {extra}')

    def _as_dict(self) -> dict[str, Any]:
        return {
            name: getattr(self, name)
            for name, attr in self.__class__.__dict__.items()
            if isinstance(attr, Field)
        }

    def __repr__(self) -> str:
        kwargs = ', '.join(
            f'{key}={value!r}' for key, value in
            self._as_dict().items()
        )
        return f'{self.__class__.__name__}({kwargs})'


if __name__ == '__main__':
    class Movie(Checked):
        title: str
        year: int
        box_office: float


    movie = Movie(title='The Godfather', year=1972,
                  box_office=137)
    print(movie.title)
    print(movie)
