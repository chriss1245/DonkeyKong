class lifes:
    '''
    The class representing the lives that Mario has
    Attributes:
        xpos - The positon in the x axis
        ypos - The positon in the y axis
        lifes . The amount of lives Mario has
        
    Methods:
        getFrames - returns a list with three tuples with the specifications of each sprite
        dgm - Updates the lives when mario clashes with a barrel
    '''
    # specifications
    __lifes = 0
    __xpos = 0
    __ypos = 0
    # sprites of the heart and the heart broken
    __animation = ((0, 191, 180, 15, 12), (0, 214, 180, 16, 12)) 

    #--------------------------------------------------------------------------
    def __init__(self, x, y, lifes = 3):
        self.__lifes = lifes
        self.__xpos = x
    #--------------------------------------------------------------------------   
    
    #--------------------------------------------------------------------------
    def getFrames(self):
        # auxiliar list wich will contain three tuples with the specifications of each heart
        info = []
        # Helps at setting the x position
        counter = 0 
        
        # Creates hearts of the lives wich mario still have
        for _ in range(self.__lifes): 
            x = self.__xpos + counter*18
            y = self.__ypos
            p, u, v, w, h = self.__animation[0]
            info.append((x, y, p, u, v, w, h))
            counter += 1
        
        # Creates hearts of the lives wich mario do not have
        for _ in range(3 - self.__lifes): 
            x = self.__xpos + counter*18
            y = self.__ypos
            p, u, v, w, h = self.__animation[1]
            info.append((x, y, p, u, v, w, h))
            counter += 1
        return info
    #--------------------------------------------------------------------------
    
    
    @property
    def lives(self):
        return self.__lifes
        
    def dmg(self): 
        con = True
        if self.__lifes == 3 and con:
            self.__lifes = 2
            con = False
        elif self.__lifes == 2 and con:
            self.__lifes = 1
            con = False
        elif self.__lifes == 1 and con:
            self.__lifes = 0
            con = False
        