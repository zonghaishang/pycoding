from typing import NamedTuple


class DemoNT(NamedTuple):
    a: int
    b: int
    c = "hello"

print(DemoNT.__annotations__)

print(DemoNT.a, DemoNT.b, DemoNT.c)

nt = DemoNT(8,9)
print(nt.a, nt.b, nt.c)
print(nt.z)