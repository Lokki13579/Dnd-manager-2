import json
class Loader:
    def load(self):
        with open(self.path) as f:
            temp = json.loads(f.read())
        for n,v in temp.items():
            self.__dict__[n] = v
class ClassLoader(Loader):
    def apply(self,target):
        d = dict(self.__dict__)
        for i in list(d.keys()).copy():
            if i.startswith("_"):
                d.pop(i)
        target.__dict__["skills"] = []
        for n,v in d.items():
            if n == "name" or n == "path":
                continue
            if n == "hp_dice":
                target.__dict__[n] = v
                continue
            elif n == "skills":
                for lev in range(target.level):
                    target.__dict__[n] += v[target.side_class][lev]
                continue
            target.__dict__[n] = v[target.level-1]

class RaceLoader(Loader):
    def apply(self,target):
        d = dict(self.__dict__)
        for i in list(d.keys()).copy():
            if i.startswith("_"):
                d.pop(i)
        target.__dict__["skills"] = []
        for n,v in d.items():
            if n == "name" or n == "path":
                continue
            target.__dict__[n] = v
