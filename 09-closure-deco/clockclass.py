import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


class clock:
    def __init__(self, fmt=DEFAULT_FMT):
        self.fmt = fmt

    def __call__(self, func):
        def clocked(*_args, **kwargs):
            t0 = time.perf_counter()
            result = func(*_args, **kwargs)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            arg_lst = [repr(arg) for arg in _args]
            arg_lst.extend(f'{k}={v!r}' for k, v in kwargs.items())
            args = ', '.join(arg_lst)
            print(self.fmt.format(**locals()))
            return result

        return clocked


if __name__ == '__main__':

    @clock()
    def snooze(seconds):
        time.sleep(seconds)


    @clock(fmt='{name}: {elapsed:0.8f}s')
    def sleeper(seconds):
        time.sleep(seconds)


    for i in range(3):
        snooze(.123)

    for i in range(3):
        sleeper(.123)
