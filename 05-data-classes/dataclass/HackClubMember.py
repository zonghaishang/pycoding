from dataclasses import dataclass
from ClubMember import ClubMember
from typing import ClassVar


@dataclass
class HackClubMember(ClubMember):
    all_handles: ClassVar[set[str]] = set()
    handle: str = ''

    def __post_init__(self):
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f'handle {self.handle!r} is already exists.'
            raise ValueError(msg)
        cls.all_handles.add(self.handle)


print(HackClubMember.__annotations__)

m1 = HackClubMember('Eiji json')
m2 = HackClubMember('Eiji micro')
