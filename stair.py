
class stair:
    __xpos = 0
    __ypos = 0
    __w = 8
    __h = 6
    
    def __init__(self,x,y):
        self.__xpos = x
        self.__ypos = y
        
    @property
    def xpos(self):
        return self.__xpos
    
    @property
    def ypos(self):
        return self.__ypos
    
    