import Memory as m

mem = m.Memory()
print(mem.__doc__)


def ret(num):
    return num


dict_mem = {}
dict_mem["self"] = 234
dict_mem["self4ef"] = 23
mem.add("tup", 17)
mem.add("srtge", "cekvbenp")
mem.add("dactup", 17)
mem.add("rtefege", "cekvbenp")
mem.add("dict", dict_mem)
print(mem.tup)
mem.delete("tup")
for x in mem.list():
    print(x)
# mem.clear()
print(mem.list())
