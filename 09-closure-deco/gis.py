registry = set()


def register(active: bool = True):
    def decorator(func):
        if active:
            print('running register', f'(active={active})->decorate({func})')
            registry.add(func)
        else:
            registry.discard(func)
        return func

    return decorator


@register(active=False)
def f1():
    print('running f1')


@register(active=True)
def f2():
    print('running f2')


if __name__ == '__main__':
    f1()
    f2()
    print(f1.__name__, f1.__doc__)
    print(f2.__name__, f2.__doc__)
