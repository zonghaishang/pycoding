import dataclasses


@dataclasses.dataclass
class ClubMember:
    name: str
    guess: list = dataclasses.field(default_factory=list)
