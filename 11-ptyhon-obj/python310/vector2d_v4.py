from array import array
import math


class Vector2d:
    typecode = 'd'
    __match_args__ = ('x', 'y')

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        # return (i for i in (self.x, self.y))
        yield self.x
        yield self.y

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash((self.x, self.y))

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, format_spec):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(i, format_spec) for i in coords)
        return outer_fmt.format(*components)

    @classmethod
    def from_bytes(cls, _octets):
        typecode = chr(_octets[0])
        memv = memoryview(_octets[1:]).cast(typecode)
        print('--->', cls.typecode, *memv)
        return cls(*memv)


def keyword_pattern_demo(v: Vector2d) -> None:
    match v:
        case Vector2d(x=0, y=0):
            print(f'{v!r} is null')
        case Vector2d(x=0):
            print(f'x={v!r} is vertical')
        case Vector2d(_, 0):
            print(f'{v!r} is horizontal')
        case Vector2d(x=x, y=y) if x == y:
            print(f'{v!r} is diagonal')
        case _:
            print(f'{v!r} is awesome')


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    v2 = Vector2d(1, 0)

    keyword_pattern_demo(v1)
    keyword_pattern_demo(v2)

    print(v1.__dict__)
