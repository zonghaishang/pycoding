from __future__ import annotations

import typing


def clip(text: str, max_len: int = 80) -> str:
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()


print(clip.__annotations__)
print(' ' * 15)
print(typing.get_type_hints(clip))
