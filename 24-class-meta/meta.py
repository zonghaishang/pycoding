class MetaBunch(type):
    def __new__(meta, cls_name, bases, cls_dict):
        defaults = {}

        def __init__(self, **kwargs):
            for _name, default in defaults.items():
                setattr(self, _name, kwargs.pop(_name, default))
            if kwargs:
                extra = ', '.join(kwargs)
                raise AttributeError(f'No slots left for:{extra!r}')

        def __repr__(self):

            rep = ', '.join(f'{_name}={value!r}'
                            for _name, default in defaults.items()
                            if (value := getattr(self, _name)) !=
                            default)
            return f'{cls_name}({rep})'

        new_dict = dict(__slots__=[],
                        __init__=__init__,
                        __repr__=__repr__)

        for name, value in cls_dict.items():
            if name.startswith('__') and name.endswith('__'):
                if name in new_dict:
                    raise AttributeError(f"Can't set {name!r} in {cls_name!r}")
                new_dict[name] = value
            else:
                new_dict['__slots__'].append(name)
                defaults[name] = value

        return super().__new__(meta, cls_name, bases, new_dict)
    



class Bunch(metaclass=MetaBunch):
    pass


if __name__ == '__main__':
    class Point(Bunch):
        x = 0.0
        y = 0.0
        color = 'gray'

        # def __init__(self):
        #     super().__init__()
        #     self.z = 0.0


    print(Point(x=1.2, y=3, color='green'))
    # p = Point(x=1.2, y=3, color='green')
    # p.u = 'panic'