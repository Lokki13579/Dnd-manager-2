from .human import Human
from .dwarf import Dwarf
from enum import Enum

class Races(Enum):
    human = Human
    dwarf = Dwarf
__all__ = ["Races"]
