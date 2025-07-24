import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):
    def decorator(func):
        def clocked(*_args, **kwargs):
            t0 = time.perf_counter()
            result = func(*_args, **kwargs)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            arg_lst = [repr(arg) for arg in _args]
            arg_lst.extend(f'{k}={v!r}' for k, v in kwargs.items())
            args = ', '.join(arg_lst)
            print(fmt.format(**locals()))
            return result

        return clocked

    return decorator


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
