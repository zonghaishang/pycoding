def tree(cls):
    yield cls.__name__, 0
    yield from sub_tree(cls, 1)


def sub_tree(cls, level):
    for child in cls.__subclasses__():
        yield child.__name__, level
        yield from sub_tree(child, level + 1)


def display(cls):
    for child, level in tree(cls):
        indent = ' ' * 4 * level
        print(f'{indent}{child}')


if __name__ == '__main__':
    display(BaseException)
