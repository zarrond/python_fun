############################################
class Memory():
    """Class used to store some data/functions/dicts in the practical way.\nUseful to store settings etc.\n"""
    
    def __init__(self):
        pass
    
    def add(self, in1, *in2):
        if callable(in1):
            setattr(self, in1.__name__, in1)
        else:
            setattr(self, in1, in2[0])
            
    def list(self):
        return self.__dict__
    
    def delete(self, name):
        try:
            delattr(self, name)
        except AttributeError:
            pass
        
    def clear(self):
        for x in list(self.__dict__):
            delattr(self, x)
            
############################################
