from .races import *
from enum import Enum

class Races(Enum):
    human = Human()
    dwarf = Dwarf()
__all__ = ["Races"]
