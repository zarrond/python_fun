from debug_tools import dprint, is_simple
from typing import Dict


class Funcs:
    def __init__(self):
        pass

    @staticmethod
    def f1(inp):
        return inp**2

    def __getitem__(self, name):
        return getattr(self, name)


'''
f = Funcs()
str1  = 'f1'
currFunc = None
if(str1 in f.__dir__()):
    currFunc = f[str1]    
    # execute
    try:
        print(currFunc(15))
    except TypeError:
        print("Func not found2")
else:
    print("Func not found1")
'''
    
# methodsDict = {}

name_counts: Dict[str, int] = {
    "Adam": 10,
    "Guido": 12
}

arr = [1, 2, 3]
dprint((), size=True)
print(is_simple(102021234122, time=True))
