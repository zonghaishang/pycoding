import sys


class LookingClass:

    def __enter__(self):
        self.origin_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.origin_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True

    def reverse_write(self, text):
        self.origin_write(text[::-1])


if __name__ == '__main__':
    with LookingClass() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)

    print('-' * 25)
    print('Alice, Kitty and Snowdrop')
