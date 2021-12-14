import random
import constants

class Barril:
    '''
    The class representing a barrel
    Attributes:
        x1 - The positon in the x axis -> xpos - gets the x1 value
        y1 - The positon in the y axis -> ypos - gets the y1 value
        w - The width
        h - The heigth
        p . number of image set
        u - coordinates in x of the frame in the image set
        v - cordinates in y of the frame in the image set
        relentization - Quantity of frames needed in order to update a sprite
        
    Methods:
        update - updates the object
        stairs_check - checks if there are stairs
        fall - It is in charge of the position in y1
        getFrame - returns the specifications needed in order to draw the sprite in the main porgram
    '''
    
    __descend = {0:(0, 128,106,), 1:(0, 153,106)} # Sprites when it is on stairs
    __rolling = {0:(0, 35, 106), 1:(0, 59,106), 2:(0, 83,106), 3:(0, 107,106)} # Sprites when it is rolling
    __vy = 0 # variation in x
    __vx = 2 # variation in y
    __stairs = [False, False, 0]  # whether there are stairs, whether you can go down and wheter the barrils wants to go down ( 1 if yes)
    __relentization = 4 # How many frames should pass in order to update the sprite
    __h = 10 # width
    __w = 12 # height

    
    
    def __init__(self, x, y):
        self.__x1 = x
        self.__y1 = y
        self.update(0)
        
        
    def update(self, nFrame):
        nFrame //= self.__relentization
        
        self.stairs_check()
                
        if self.__stairs[0] and self.__stairs[1] and self.__stairs[2] == 1:
            self.__w = 17
            self.__h = 10
            self.__vx = 0
            self.__y1 += constants.Y
            script = nFrame %  2
            
            self.__p, self.__u, self.__v = self.__descend[script]
            
            
        else:
           
            self.__stairs[2] = random.randint(0,1)
            self.fall()
            self.__w = 12
            self.__h = 10
            
        
            script = nFrame %  4
            self.__p, self.__u, self.__v = self.__rolling[script]
    
        
        if self.__stairs[0] == False and self.__vx == 0:
            number = random.randint(0, 1)
            if number == 1:
                self.__vx = -2
            else:
                self.__vx = 2
                
        if self.__x1 <= 0 and self.__vx != 2:
            self.__vx = 2
        elif self.__x1 + self.__w >= constants.WIDTH and self.__vx != -2:
            self.__vx = -2
            
        
        self.__x1 += self.__vx
        
    
        
    def stairs_check(self):
        stair = False
        down = False
        
        if self.__y1 + self.__h in range(201 , 238) and (self.__x1 == 32):
            stair = True
            if self.__y1 + self.__h in range(201, 238):
                down = True
        
        elif self.__y1+ self.__h in range(153, 193) and self.__x1 == 154: # 2nd stair
            stair = True
            if self.__y1 + self.__h in range(153, 193):
                down = True
                
        elif self.__y1 + self.__h in range(103, 149) and self.__x1 == 60: # 3rd stair
            stair = True
            if self.__y1 + self.__h in range(103, 149):
                down = True
                
        elif self.__y1 + self.__h in range(61, 99)  and (self.__x1 == constants.WIDTH - 54): # 4th stair
            stair = True
            if self.__y1 + self.__h in range(61, 99):
                down = True
    
        self.__stairs = [stair, down, self.__stairs[2]]
        
    
    def fall(self):
        
        #They are only conditionals with fixed values. We'd liked to use a for loop in this task but we werent able of finding the right pattern
        # I am not proud of this to be honest. I think it could have been done of a better way
        if self.__y1 + self.__h >= 55 and self.__y1 + self.__h < 65:
            c = int(constants.WIDTH/2.5) + 16
            x2 = self.__x1 + self.__w
            x1 = self.__x1
            
            if x1 in range(0, c)  or x2 in range(0, c):
                self.__y1 = 48
            elif x1 in range(c, c + 8*3) or x2 in range(c, c + 8*3 + 1):
                self.__y1 = 49
            elif x1 in range(c + 8*6) or x2 in range(c + 8*6 + 1):
                self.__y1 = 50
            elif x1 in range( c + 8*9) or x2 in range(c + 8*9 + 1):
                self.__y1 = 51
            else:
                self.__y1 += 2
                
        elif self.__y1 + self.__h > 95 and self.__y1 + self.__h <= 110:
            c = constants.WIDTH
            x2 = self.__x1 + self.__w
            x1 = self.__x1
            
            
            if x1 in range(c, c - 8)  or x2 in range(c, c - 8):
                self.__y1 = 90
            elif x1 in range(c - 8*3, c - 8 + 1  ) or x2 in range(c - 8*3, c - 8 + 1  ):
                self.__y1 = 91
            elif x1 in range(c - 8*6, c - 8*3 + 1) or x2 in range(c - 8*6, c - 8*3 + 1):
                self.__y1 = 92
            elif x1 in range( c - 8*9, c - 8*6 + 1) or x2 in range( c - 8*9, c - 8*6 + 1):
                self.__y1 = 93
            elif x1 in range( c - 8*12, c - 8*9 + 1) or x2 in range( c - 8*12, c - 8*9 + 1):
                self.__y1 = 94
            elif x1 in range( c - 8*15, c - 8*12+ 1) or x2 in range( c - 8*15, c - 8*12 + 1):
                self.__y1 = 95
            elif x1 in range( c - 8*18, c - 8*15 + 1) or x2 in range( c - 8*18, c - 8*15 + 1):
                self.__y1 = 96
            elif x1 in range( c - 8*21, c - 8*18 + 1) or x2 in range( c - 8*21, c - 8*18 + 1):
                self.__y1 = 97
            else:
                self.__y1 += 2 
       
        
        elif self.__y1 + self.__h > 147 and self.__y1 + self.__h <= 180:
            c = 0
            x2 = self.__x1 + self.__w
            x1 = self.__x1
            
            if x1 in range(c + 8 + 1)  or x2 in range( c + 8 + 1):
                self.__y1 = 139
            elif x1 in range(c + 8*3 + 1) or x2 in range(c + 8*3 + 1):
                self.__y1 = 140
            elif x1 in range(c + 8*6 + 1) or x2 in range(c + 8*6 + 1):
                self.__y1 = 141
            elif x1 in range( c + 8*9 + 1) or x2 in range(c + 8*9 + 1):
                self.__y1 = 142
            elif x1 in range( c + 8*12 + 1) or x2 in range(c + 8*12 + 1):
                self.__y1 = 143
            elif x1 in range( c + 8*15 + 1) or x2 in range(c + 8*15 + 1):
                self.__y1 = 144
            elif x1 in range( c + 8*18 + 1) or x2 in range(c + 8*18 + 1):
                self.__y1 = 145
            elif x1 in range( c + 8*21 + 1) or x2 in range(c + 8*21 + 1):
                self.__y1 = 146
            else:
                self.__y1 += 2
                
        elif self.__y1 + self.__h > 192 and self.__y1 + self.__h <= 215:
            c = constants.WIDTH
            x2 = self.__x1 + self.__w
            x1 = self.__x1
            
            
            if x1 in range(c, c - 8)  or x2 in range(c, c - 8):
                self.__y1 = 184
            elif x1 in range(c - 8*3, c - 8 + 1  ) or x2 in range(c - 8*3, c - 8 + 1  ):
                self.__y1 = 185
            elif x1 in range(c - 8*6, c - 8*3 + 1) or x2 in range(c - 8*6, c - 8*3 + 1):
                self.__y1 = 186
            elif x1 in range( c - 8*9, c - 8*6 + 1) or x2 in range( c - 8*9, c - 8*6 + 1):
                self.__y1 = 187
            elif x1 in range( c - 8*12, c - 8*9 + 1) or x2 in range( c - 8*12, c - 8*9 + 1):
                self.__y1 = 188
            elif x1 in range( c - 8*15, c - 8*12+ 1) or x2 in range( c - 8*15, c - 8*12 + 1):
                self.__y1 = 189
            elif x1 in range( c - 8*18, c - 8*15 + 1) or x2 in range( c - 8*18, c - 8*15 + 1):
                self.__y1 = 190
            elif x1 in range( c - 8*21, c - 8*18 + 1) or x2 in range( c - 8*21, c - 8*18 + 1):
                self.__y1 = 191
            else:
                self.__y1 += 2     
        
        elif self.__y1 + self.__h > 233 and self.__y1 + self.__h <= 255:
            c = 0
            x2 = self.__x1 + self.__w
            x1 = self.__x1
            
            if x1 in range(c + 8 + 1)  or x2 in range( c + 8 + 1):
                self.__y1 = 229
            elif x1 in range(c + 8*3 + 1) or x2 in range(c + 8*3 + 1):
                self.__y1 = 230
            elif x1 in range(c + 8*6 + 1) or x2 in range(c + 8*6 + 1):
                self.__y1 = 231
            elif x1 in range( c + 8*9 + 1) or x2 in range(c + 8*9 + 1):
                self.__y1 = 232
            elif x1 in range( c + 8*12 + 1) or x2 in range(c + 8*12 + 1):
                self.__y1 = 233
            elif x1 in range( c + 8*15 + 1) or x2 in range(c + 8*15 + 1):
                self.__y1 = 234
            elif x1 in range( c + 8*21 + 1) or x2 in range(c + 8*26 + 1):
                self.__y1 = 235
            else:
                self.__y1 += 10
        else:
            self.__y1 += 2 
    
    def getFrame(self):
        t = (self.__x1, self.__y1, self.__p, self.__u, self.__v, self.__w, self.__h)
        return t

    
    @property
    def ypos(self):
        return self.__y1
    @property
    def xpos(self):
        return self.__x1
    
    