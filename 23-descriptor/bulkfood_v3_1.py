class Quantity:
    # def __init__(self, storage_name):
    #     self.storage_name = storage_name

    def __set_name__(self, owner, name):
        self.storage_name = name

    # def __get__(self, instance, owner):
    #     if instance is None:
    #         return self
    #     return instance.__dict__[self.storage_name]

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise AttributeError("value must be > 0")


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == "__main__":
    nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)
    print(nutmeg.subtotal())
