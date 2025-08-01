from typing import TypedDict


class BookDict(TypedDict):
    isbn: str
    title: str
    authors: list[str]
    pagecount: int


pp = BookDict(isbn='0201657880', title='Programming Pearls', authors='Jon Bentley', pagecount=256)
print(type(pp), pp)
