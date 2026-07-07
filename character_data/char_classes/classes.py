from ..loader import ClassLoader

__all__ = ["Bard","Sorcerer"]
class Bard(ClassLoader):
    def __init__(self):
        self.path = "/home/artem/Projects/dnd-manager/jsons/classes/bard.json"
        self.load()

class Sorcerer(ClassLoader):
    def __init__(self):
        self.path = "/home/artem/Projects/dnd-manager/jsons/classes/sorcerer.json"
        self.load()

class Artificer(ClassLoader):
    def __init__(self):
        self.path = "/home/artem/Projects/dnd-manager/jsons/classes/artificer.json"
        self.load()