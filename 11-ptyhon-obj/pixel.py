class Pixel:
    __slots__ = ('x', 'y')


class OpenPixel(Pixel):
    __slots__ = ('color',)
    pass


p = Pixel()
p.x = 10
p.y = 20
print(p)
# print(p.__dict__)

op = OpenPixel()
op.color = 'red'
print(op.__dict__)
