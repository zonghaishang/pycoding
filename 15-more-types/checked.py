import inspect
import typing


class Checked:
    @classmethod
    def _fields(cls) -> dict[str, type]:
        return typing.get_type_hints(cls)
        # return inspect.get_annotations(cls)
