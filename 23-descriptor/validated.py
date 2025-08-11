import abc


class Validated(abc.ABC):
    @abc.abstractmethod
    def validate(self, name, value):
        """返回通过验证的值，或者抛出ValueError"""

    def __set_name__(self, owner, name):
        self.storage_name = name

    def __set__(self, instance, value):
        value = self.validate(self.storage_name, value)
        instance.__dict__[self.storage_name] = value
