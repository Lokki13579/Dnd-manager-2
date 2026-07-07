from ..loader import ClassLoader

__all__ = ["Artificer","Bard","Sorcerer"]
class Artificer(ClassLoader):
    def __init__(self):
        self.path = "/home/artem/Projects/dnd-manager/jsons/classes/artificer.json"
        self.load()

class Bard(ClassLoader):
    def __init__(self):
        self.path = "/home/artem/Projects/dnd-manager/jsons/classes/bard.json"
        self.load()

class Sorcerer(ClassLoader):
    def __init__(self):
        self.path = "/home/artem/Projects/dnd-manager/jsons/classes/sorcerer.json"
        self.load()
