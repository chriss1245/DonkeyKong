

class suelo:
    '''
    The class represents the ground of the stage of the game
    Attributes:
        xpos - the position on the x axis
        ypos - the position on the y axis
        level - the plataform that its representing
        
    Methods:
        @property methods - give an attribute back
    '''
    __xpos = 0
    __ypos = 0
    __level = 0
    
    def __init__(self,x,y, level):
        self.__xpos = x
        self.__ypos = y
        self.__level = level
        
    @property
    def xpos(self):
        return self.__xpos
    
    @property
    def ypos(self):
        return self.__ypos
    
    @property
    def level(self):
        return self.__level