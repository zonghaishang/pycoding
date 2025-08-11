from validated import Validated


class Quantity(Validated):

    def validate(self, name, value):
        if value < 0:
            raise ValueError(f'{name} must be > 0')
        return value


class NonBlank(Validated):

    def validate(self, name, value):
        value = value.strip()
        if not value:
            raise ValueError(f'{name} cannot be empty')
        return value
