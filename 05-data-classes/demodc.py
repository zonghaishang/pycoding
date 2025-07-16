# from dataclasses import dataclass
import dataclasses


@dataclasses.dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = 'spam'


print(DemoDataClass.__annotations__)
print(DemoDataClass.b, DemoDataClass.c)

d = DemoDataClass(1, 2)
print((d.a, d.b))

# print(DemoDataClass.a)
