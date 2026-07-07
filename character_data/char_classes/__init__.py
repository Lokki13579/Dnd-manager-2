from .classes import *
from enum import Enum

class Classes(Enum):
    bard = Bard()
    sorcerer = Sorcerer()

__all__ = ["Classes"]