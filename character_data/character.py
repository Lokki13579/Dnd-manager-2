from .char_classes import *
from .races import *

class Character:
    def __init__(self,
    name="Базовое имя",
    char_class = Classes.bard,
    race = Races.human,
    level = 1):

        self.name = name
        self.charclass = char_class.value
        self.race = race.value
        self.level = level
        self.apply_level()

    def get_master_bonus(self):
        return (self.level - 1) // 4 + 2

    def set_level(self,new_level):
        if not (1 <= new_level <= 20):
            return
        self.level = new_level
        self.apply_level()
    def apply_level(self):
        self.master_bonus = self.get_master_bonus()
    def set_class(self,new_class):
        if type(new_class) == str:
            for t in Classes:
                n,v = t.name, t.value
                if n == new_class:
                    self.charclass = v
    def set_race(self,new_race):
        if type(new_race) == str:
            for t in Races:
                n,v = t.name, t.value
                if n == new_race:
                    self.race = v

        


