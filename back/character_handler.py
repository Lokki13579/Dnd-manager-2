import os
import json
import math
from .SETTINGS import get_levels_data, SAVES_DIR
from .loader import get_full_class_info, get_full_race_info
LEVELS = get_levels_data()
class character(dict):
    """Словарь с предустановленными для персонажа параметрами"""
    all_characters = []
    def __init__(self,id, mapping=None,/,**kwargs):
        nmap = {
            'id':id,
            'name':"Безымянный",
            'class':'Бард',
            'side_class':'none',
            'race':'Человек',
            'level':1,
            'exp':0,
            'common_exp':0,
            'strength':8,
            'agility':8,
            'constitution':8,
            'charisma':8,
            'intelligence':8,
            'wisdom':8,
        }
        if mapping is not None:
            nmap.update(mapping)
        if kwargs:
            nmap.update({kay:value for key,value in kwargs.items()})
        super().__init__(nmap)
        character.all_characters.append(self)
        h = Handler(self)
        h.init_character()
        del h

class Handler:
    def __init__(self,data):
        if isinstance(data,int):
            self.id = id
            self.char = self.__find_char_by_id()
        elif isinstance(data,dict):
            self.id = -1
            self.char = data
    def __find_char_by_id(self):
        for char in character.all_characters:
            if char.get("id") == self.id:
                return char
    def init_character(self):
        self.update_race()
        self.update_class()
    def add_level(self,amount=1):
        cur_lev = self.char.get('level',1)
        self.set_level(cur_lev+amount)
    def set_level(self,new_value):
        if not (1 <= new_value <= 20):
            return
        levels = get_levels_data()
        cexp = levels.get(new_value)+self.char.get('exp')
        self.set_common_exp(cexp)
    def set_exp(self,new_value):
        levels = get_levels_data()
        cexp = levels.get(self.char.get('level'))+new_value
        self.set_common_exp(cexp)
    def set_common_exp(self,new_value):
        self.char.update({'common_exp':new_value})
        self.update_common_exp()
    def update_common_exp(self):
        _levels = list(LEVELS.items())[::-1]
        for lev, exp in _levels:
            if exp > self.char.get('common_exp'):
                continue
            self.char.update({
                'level':lev,
                'exp':self.char.get('common_exp',exp)-exp
            })
            self.update_level()
            break
    def update_level(self):
        self.char.update({'master_bonus':math.ceil(self.char.get('level')/4)+1})
        self.update_class()

    def update_race(self):
        data = get_full_race_info(self.char.get('race'))
        data['race'] = data['name']
        del data['name']
        for n,v in data.items():
            self.char.update({n:v})

    def update_class(self):
        data = get_full_class_info(self.char.get('class'))
        data['class'] = data['name']
        del data['name']
        const_chars = data.pop('const_chars')
        special_chars = data.pop('special_chars')
        for ch in const_chars:
            if ch in self.char:
                continue
            self.char.update({ch:data.pop(ch)})

        self.char['skills'] = []
        skills = data.pop('skills')
        for l in range(self.char.get('level')):
            self.char['skills'] += skills.get(self.char.get('side_class','none'))[l]

        for n,v in data.items():
            if n in self.char.get('side_classes',[]):
                for _n,_v in data.get(n).items():
                    self.char.update({n:v[self.char.get('level',1)-1]})
                continue
            self.char.update({n:v[self.char.get('level',1)-1]})



# GET
def create_character(name='Безымянный'):
    all_id = [c.get('id',-1) for c in character.all_characters] + [2]
    for i in range(1,max(all_id)+2):
        if i in all_id:
            continue
        available_id = i
        break
    new_character = character(available_id,{'name':name})
    print(f"created Character - {new_character.get('name')}, id = {available_id}")
    return new_character


# UPDATE
def save_characters():
    with open(SAVE_CHAR_PATH,w,encoding="utf-8"):
        pass
def load_characters():
    files = os.listdir(SAVES_DIR)
    for file in files:
        with open(SAVES_DIR+file) as f:
            character.all_characters.append(json.loads(f.read()))

