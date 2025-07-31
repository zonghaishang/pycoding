import tkinter


class Root:
    def ping(self):
        print(f'{self}.ping() in Root')

    def pong(self):
        print(f'{self}.pong() in Root')

    def __repr__(self):
        cls_name = type(self).__name__
        return f'<instance of {cls_name}>'


class A(Root):
    def ping(self):
        print(f'{self}.ping() in A')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in A')
        super().pong()


class B(Root):

    def ping(self):
        print(f'{self}.ping() in B')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in B')


class U:  # mixin
    def ping(self):
        print(f'{self}.ping() in U')
        super().ping()


class Leaf(A, B):
    def ping(self):
        print(f'{self}.ping() in Leaf')
        super().ping()


class LeafUA(U, A):
    def ping(self):
        print(f'{self}.ping() in UA')
        super().ping()


def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))


print_mro(tkinter.Text)

# leaf1 = Leaf()
# leaf1.ping()
#
# print(' ' * 15)
# leaf1.pong()


u = LeafUA()
u.ping()
print(' ' * 15)
u.pong()
