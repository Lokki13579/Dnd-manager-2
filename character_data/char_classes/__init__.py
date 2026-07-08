from .classes import *
from enum import Enum

class Classes(Enum):
    bard = Bard()
    sorcerer = Sorcerer()
    artificer = Artificer()
    wizard = Wizard()
    cleric = Cleric()
    barbarian = Barbarian()
    fighter = Fighter()
    druid = Druid()
    warlock = Warlock()
    monk = Monk()
    paladin = Paladin()
    rogue = Rogue()
    ranger = Ranger()

__all__ = ["Classes"]