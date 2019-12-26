class Paulone:
    '''
    The class representing Pauline, the princess
    Attributes:
        x - The positon in the x axis -> xpos - gets x
        y - The positon in the y axis
        w - the width of the mario sprites
        h - the heigth of the mario sprites
        p - position of the sprite in the image set
        u, v - coordinates x, y of the sprite in the image set
        
    Methods:
        getFrame - returns the specifications requiared in order to draw the sprite
        update - updates the possition and the sprite
    '''
    
    __animation = ([2, 2, 194], [2, 24, 193], [2, 49, 193], 
                   [0, 6, 179], [0, 31, 179], [0, 54, 179]) # The sprites
    #initial parameters
    __x = 131
    __vx = -2 # variation in x
    __y = 2
    __w = 16
    __h = 23
    __p = 2
    __u = 2
    __v = 194
    def __init__(self):
        self.update(0) # In order to avoid problems with the initialization we update once at the init
        
    def update(self, frames):
        
        # Limits of Paulone's walking
        if self.__x <= 140 and self.__vx != 2:
            if frames % 100 == 99: # Stops by 99 frames
                self.__vx = 2
            else:
                self.__vx = 0
                self.__p, self.__u, self.__v = self.__animation[2] # Script when Paulone stoped
        elif self.__x + self.__w >= 190 and self.__vx != -2:
            if frames % 100 == 99:
                self.__vx = -2
            else:
                self.__vx = 0
                self.__p, self.__u, self.__v = self.__animation[5]
        
        # Animation of paulone walking
        frames //= 4
        if self.__vx == 2:
            script = frames % 2 + 3
            self.__p, self.__u, self.__v = self.__animation[script]
        elif self.__vx == -2:
            script = frames % 2
            self.__p, self.__u, self.__v = self.__animation[script]
        
        
        
        # Updating the position
        self.__x += self.__vx
        
    def getFrame(self):
        return self.__x, self.__y, self.__p, self.__u, self.__v, self.__w, self.__h
    
    @property
    def xpos(self):
        return self.__x