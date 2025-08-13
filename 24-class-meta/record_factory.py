from typing import Union, Any
from collections.abc import Iterable, Iterator

FieldNames = Union[str, Iterable[str]]


def record_factory(class_name: str, field_names: FieldNames) -> type:  # ignore
    slots = parse_identifier(field_names)

    def __init__(self, *args, **kwargs) -> None:
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self) -> Iterator[Any]:
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self) -> str:
        values = ', '.join(f'{name}={value!r}' for name, value in zip(self.__slots__, self))
        _class_name = self.__class__.__name__
        return f'{_class_name}({values})'

    cls_attrs = dict(
        __slots__=slots,
        __init__=__init__,
        __iter__=__iter__,
        __repr__=__repr__,
    )

    return type(class_name, (object,), cls_attrs)


def parse_identifier(names: FieldNames) -> tuple[str, ...]:
    if isinstance(names, str):
        names = names.replace(',', ' ').split()
    if not all(s.isidentifier() for s in names):
        raise ValueError('names must all be valid identifiers')
    return tuple(names)


if __name__ == '__main__':
    Dog = record_factory('Dog', 'name weight owner')
    print(Dog)
    rex = Dog('Rex', 30, 'Bob')
    print(rex)
