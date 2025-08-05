import contextlib
import sys


@contextlib.contextmanager
def looking_class():
    origin_write = sys.stdout.write

    def reverse_write(text):
        origin_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = origin_write
        if msg:
            print(msg)


if __name__ == '__main__':
    with looking_class() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)

    print('-' * 25)
    print('Alice, Kitty and Snowdrop')
