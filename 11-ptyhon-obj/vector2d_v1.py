from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

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
        return hash(tuple(self))

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


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    print(v1)

    print('format: ', format(v1))
    print('format: ', format(v1, '.2f'))
    print('format: ', format(v1, 'p'))

    print(hash(v1))

    x, y = v1
    print(x, y)
    v1_clone = eval(repr(v1))
    print(v1_clone)
    octets = bytes(v1)
    print(octets)

    v3 = Vector2d.from_bytes(octets)
    print(v3)

    print(abs(v1))
    print(bool(v1), bool(Vector2d(0, 0)))
