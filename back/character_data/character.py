from .char_classes import *
from .races import *
import json
import math

class Character:
    def __init__(self,
    id,
    name="Базовое имя",
    char_class = Classes.bard,
    race = Races.human,
    level = 1):

        self.id = id
        self.name = name
        self._char_class = "bard"
        self.side_class = "none"
        self._race = "human"
        self.level = level
        self.common_exp = 0
        self.exp = 0
        self.set_strength(8)
        self.set_agility(8)
        self.set_constitution(8)
        self.set_charisma(8)
        self.set_intelligence(8)
        self.set_wisdom(8)
        self.apply_character()




    def load_levels_data(self):
        with open("/home/artem/Projects/dnd-manager/jsons/levels") as f:
            f.readline()
            levels_data = {}
            for line in f.readlines():
                lev, exp = line.split()
                lev, exp = int(lev), int(exp)
                levels_data[lev] = exp
        return levels_data
    def get_side_classes(self):
        return list(self.side_classes.items())
    def set_side_class(self,new_side_class):
        for side in self.get_side_classes():
            if new_side_class in side:
                self.side_class = side[0]
                break
        else:
            self.side_class = "none"
        self.apply_character()

    def get_common_exp(self):
        levels_data = self.load_levels_data()
        return levels_data[self.level] + self.exp
    def update_common_exp(self):
        levels_data = self.load_levels_data()
        self.common_exp = levels_data[self.level] + self.exp

    def get_master_bonus(self):
        return (self.level - 1) // 4 + 2

    def apply_character(self):
        self.apply_level()
        self.apply_class()
        self.apply_race()
    def apply_level(self):
        self.master_bonus = self.get_master_bonus()
        self.update_common_exp()
    def apply_class(self):
        self.char_class.apply(self)
    def apply_race(self):
        self.race.apply(self)
    
    def set_level(self,new_level):
        if not (1 <= new_level <= 20):
            return False
        self.level = new_level
        self.apply_character()
        return True
    def set_exp(self,new_value):
        self.exp = new_value
        self.set_common_exp(self.get_common_exp())
    def set_common_exp(self,new_value):
        if not (0 <= new_value <= 355_000):
            return False
        self.common_exp = new_value
        self.reload_level()
        return True
    def set_class(self,new_class):
        if type(new_class) == str:
            for t in Classes:
                n,v = t.name, t.value
                if n == new_class:
                    self.char_class = v
        self.apply_character()
    def set_race(self,new_race):
        if type(new_race) == str:
            for t in Races:
                n,v = t.name, t.value
                if n == new_race:
                    self.race = v
    def set_characteristic(self,char,new_value):
        if char not in ['intelligence','wisdom','charisma','agility','strength','constitution']:
            return
        if not ( 1 <= new_value <= 20):
            return
        mod = math.floor(new_value-10)//2
        self.__dict__[char] = [new_value, mod]

    def set_intelligence(self,new_value):
        self.set_characteristic("intelligence",new_value)
    def set_wisdom(self,new_value):
        self.set_characteristic("wisdom",new_value)
    def set_charisma(self,new_value):
        self.set_characteristic("charisma",new_value)
    def set_agility(self,new_value):
        self.set_characteristic("agility",new_value)
    def set_strength(self,new_value):
        self.set_characteristic("strength",new_value)
    def set_constitution(self,new_value):
        self.set_characteristic("constitution",new_value)

    def reload_level(self):
        levels_data = self.load_levels_data()
        levels_data = list(levels_data.items())
        levels_data = levels_data[::-1]
        for l, e in levels_data:
            if e <= self.common_exp:
                self.level = l
                self.exp = self.common_exp - e
                self.apply_character()
                break
    def replaceRaceToObj(self):
        for t in Races:
            n,v = t.name, t.value
            if self.race == n:
                self.race = v
                break
    def replaceClassToObj(self):
        for t in Classes:
            n,v = t.name, t.value
            if self.char_class == n:
                self.char_class = v
                break
    def replaceRaceToStr(self):
        for t in Races:
            n,v = t.name, t.value
            if self.race == v:
                self.race = n
                break
    def replaceClassToStr(self):
        for t in Classes:
            n,v = t.name, t.value
            if self.char_class == v:
                self.char_class = n
                break

    def load_character_from_file(self,file):
        with open(file) as f:
            data = json.loads(f.read())
        self.__dict__ = data
        self.replaceClassToObj()
        self.replaceRaceToObj()
        print(self.__dict__)
        return True
        
    def save_char(self,path=None):
        if not path:
            path = "/home/artem/Projects/dnd-manager/jsons/saves/"+self.name.replace(" ","-")+".json"
        self.replaceClassToStr()
        self.replaceRaceToStr()
        self.write_file(self.__dict__,path)
    def write_file(self,data,path):
        with open(path,"w",encoding="UTF-8") as f:
            json.dump(data,f,indent=4,ensure_ascii=False)



