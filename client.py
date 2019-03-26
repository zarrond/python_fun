class ArgParser():
    
    def __init__(self, comm):
        self.__command = comm
        self.__Args = []
        
    def getCmd(self):
        '''not used, only debugging'''
        return self.__command
    
    def getArgs(self):
        '''not used, only debugging'''
        return self.__Args
    
    def addArg(self, Arg):
        setattr(self, Arg, None)
        self.__Args.append(Arg)
        
    def parseArgs(self):
        import re
        cmd = self.__command
        for x in self.__Args:
            m = re.search('(-+){} (\w+)( --?| ?)'.format(x), cmd)
            if m:
                found = m.group(2)
                setattr(self, x, found)
    
          
    
a = ArgParser("python j.py -  k 21 --value 3")
print(a.getCmd())
a.addArg("__k")
a.addArg("value")
print(a.__k)
print(a.value)
print(a.getArgs())

a.parseArgs()
print(a.__k)
print(a.value)
print(a.__dict__.keys())