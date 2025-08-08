import json
from collections import abc
import keyword


class FrozenJSON3:

    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self._data = {}
        for key, val in mapping.items():
            if keyword.iskeyword(key):
                key = key + '_'
            self._data[key] = val

    def __getattr__(self, name):
        try:
            return getattr(self._data, name)
        except AttributeError:
            return FrozenJSON3(self._data[name])

    def __dir__(self):
        return self._data.keys()


def load(path: str):
    with open(path) as fp:
        return json.load(fp)


if __name__ == '__main__':
    # data = load("osconfeed-sample.json")
    js = FrozenJSON3({'name': 'Jim Bo', 'class': 1982})
    js.abc = 'abc'
    print(js.name, js.class_, js.abc)
