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
        extras = list(target.__dict__.keys())[16:]
        for k in extras:
            target.__dict__.pop(k)
        target.__dict__["skills"] = []
        for n,v in d.items():
            if n in ["name", "path"]:
                continue
            if n in ["hp_dice","side_classes","spells"]:
                target.__dict__[n] = v
                continue
            elif n == "skills":
                for lev in range(target.level):
                    target.__dict__[n] += v[target.side_class][lev]
                continue
            if n in d.get("side_classes"):
                continue
            target.__dict__[n] = v[target.level-1]
        for_side_class = d.get(target.side_class,{})
        for n,v in for_side_class.items():
            target.__dict__[n] = v[target.level-1]


class RaceLoader(Loader):
    def apply(self,target):
        d = dict(self.__dict__)
        for i in list(d.keys()).copy():
            if i.startswith("_"):
                d.pop(i)
        for n,v in d.items():
            if n == "name" or n == "path":
                continue
            target.__dict__[n] = v
