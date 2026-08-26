class Cell:
    EMPTY = 0
    PACGUM = 1
    SUPER_PACGUM = 2

    def __init__(self, walls: int, content: int = EMPTY) -> None:
        self.north: bool = bool(walls & 1)
        self.east: bool = bool(walls & 2)
        self.south: bool = bool(walls & 4)
        self.west: bool = bool(walls & 8)
        self.is_pattern: bool = (walls == 15)
        self.content: int = content

    def has_wall(self, direction: str) -> bool:
        return {
            "N": self.north,
            "E": self.east,
            "S": self.south,
            "W": self.west,
        }.get(direction, True)

    def __repr__(self) -> str:
        return (
            f"Cell(N={self.north}, E={self.east}, "
            f"S={self.south}, W={self.west}, content={self.content})"
        )
