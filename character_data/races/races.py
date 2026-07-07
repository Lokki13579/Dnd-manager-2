from ..loader import RaceLoader

__all__ = ["Human","Dwarf"]
class Human(RaceLoader):
    def __init__(self):
        self.path = "/home/artem/Projects/dnd-manager/jsons/races/human.json"
        self.load()

class Dwarf(RaceLoader):
    def __init__(self):
        self.path = "/home/artem/Projects/dnd-manager/jsons/races/dwarf.json"
        self.load()
        