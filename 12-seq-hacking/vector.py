import operator
from array import array
import reprlib
import math


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)
            return cls(self._components[key])
        index = operator.index(key)
        return self._components[index]

    def __len__(self):
        return len(self._components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return f'Vector({components})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    def __hash__(self):
        return hash(tuple(self))

    @classmethod
    def from_bytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v = Vector(range(10))
    print(v[1:5])
    # v1 = Vector([3.0, 4.0])
    # print(v1)
    #
    # print(hash(v1))
    #
    # x, y = v1
    # print(x, y)
    # v1_clone = eval(repr(v1))
    # print(v1_clone)
    # octets = bytes(v1)
    # print(octets)
    #
    # v3 = Vector.from_bytes(octets)
    # print(v3)
    #
    # print(abs(v1))
    # print(bool(v1), bool(Vector([0, 0])))
