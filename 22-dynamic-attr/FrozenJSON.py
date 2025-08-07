import json
from collections import abc


class FrozenJSON:

    def __init__(self, mapping):
        self._data = dict(mapping)

    def __getattr__(self, name):
        try:
            return getattr(self._data, name)
        except AttributeError:
            return FrozenJSON.build(self._data[name])

    def __dir__(self):
        return self._data.keys()

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


def load(path: str):
    with open(path) as fp:
        return json.load(fp)


if __name__ == '__main__':
    data = load("osconfeed-sample.json")
    js = FrozenJSON(data)
    print(type(data), js.Schedule.events[0].name)
