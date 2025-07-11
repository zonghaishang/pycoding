class StrKeyDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


mydict = StrKeyDict()
mydict.setdefault(1,2)
mydict.setdefault("2",3)

print("mydict[1]=", mydict[1])
print("mydict['2']=", mydict["2"])
print("mydict.get(\"3\", \"None\")=", mydict.get("3", "None"))