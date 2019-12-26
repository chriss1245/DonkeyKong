class points:
    '''
    The class that represents the counter of points
    Attributes:
        xpos - the positon to of the counter in the x axis
        ypos - the positon to of the counter in the y axis
        score - the amount of points mario has
        
    Methods:
        scorepoints - recives an input and sums it to the total amount of points
        socrereset - puts the total amount of points back to 0
         @Property methods - return an attribute
    '''
    __xpos = 0
    __ypos = 0
    __score = 0
    
    def __init__(self, x, y, score = 0):
        self.__xpos = x
        self.__ypos = y
        self.__score = score
        
    @property
    def score(self):
        return self.__score
    
    @property
    def xpos(self):
        return self.__xpos
    
    @property
    def ypos(self):
        return self.__ypos
    
    def scorespoint(self, c):
        self.__score += c
        
    def scorereset(self):
        self.__score = 0