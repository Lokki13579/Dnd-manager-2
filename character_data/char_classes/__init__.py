from .bard import Bard
from .sorcerer import Sorcerer
from enum import Enum

class Classes(Enum):
    bard = Bard
    sorcerer = Sorcerer
__all__ = ["Classes"]