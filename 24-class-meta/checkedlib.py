from collections.abc import Callable
from typing import Any, NoReturn, get_type_hints


class Field:

    def __init__(self, name: str, constructor: Callable) -> None:
        if not callable(constructor) or constructor is type(None):
            raise TypeError(f'{name!r} type hint must be callable')
        self.name = name
        self.constructor = constructor

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
        instance.__dict__[self.name] = value


class Checked:

    @classmethod
    def _fields(cls) -> dict[str, type]:
        return get_type_hints(cls)

    def __init_subclass__(sub_cls, **kwargs) -> None:
        super().__init_subclass__()
        for name, constructor in sub_cls._fields().items():
            setattr(sub_cls, name, Field(name, constructor))

    def __setattr__(self, name: str, value: Any) -> None:
        if name in self._fields():
            cls = self.__class__

            descriptor = getattr(cls, name)
            descriptor.__set__(self, value)
        else:
            self.__flag_unknown_attrs(name)

    def __init__(self, **kwargs) -> None:
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


class Movie(Checked):
    title: str
    year: int
    box_office: float


if __name__ == '__main__':
    movie = Movie(title='The Godfather', year=1972,
                  box_office=137)
    print(movie.title)
    print(movie)

    # ops, not allowed
    movie.color = 'red'
