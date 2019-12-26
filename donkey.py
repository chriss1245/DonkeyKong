
class Donkey():
    '''
    The class representing Donkey Kong
    Attributes:
        x - The positon in the x axis -> xpos - gets x
        y - The positon in the y axis
        w - the width of the mario sprites
        h - the heigth of the mario sprites
        p - position of the sprite in the image set
        u, v - coordinates x, y of the sprite in the image set
        
    Methods:
        update - Updates the object, returns true if it is time of creating a barrel
        getFrame - gives the information required to draw
    '''
    __animation = [(0, 3, 58, 46, 32), (0, 200, 58, 46, 32), 
                   (0, 52, 58, 46, 32), (0, 8, 213, 46, 32),
                   (2, 10, 68, 46, 32), (0, 105, 58, 40, 32),
                   (0, 150, 58, 46, 32)]
    __x = 28
    __y = 26
    def __init__(self):
        self.update(0) # Update in order to avoid errors
    
    def update(self, nFrames):
        h = nFrames // 10 # Relentizes the frames upload ten times
        h %= 7 # gives the index of the sprite we are going to use
        self.__p, self.__u, self.__v,self.__w, self.__h = self.__animation[h]
        
        # The time in which Donkey Kong should throw the barril
        if  nFrames % 70 == 45:
            return True
        else:
            return False
    
    def getFrame(self):
        return self.__x, self.__y, self.__p, self.__u, self.__v,self.__w, self.__h