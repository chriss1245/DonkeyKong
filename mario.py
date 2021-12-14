import constants

class mario: 
    '''
    The class representing the plater character (Mario)
    Attributes:
        xpos - The positon in the x axis
        ypos - The positon in the y axis
        originalx - the original x pos
        originaly - the original y pos
        w - the width of the mario sprites
        h - the heigth of the mario sprites
        sprite - the sprite mario is currently using (to animate movement)
        direction - the direction mario is moving (0 - left, 1 - right)
        jump_interval - the amount of time that mario can be jumping
        level_ground - the platform where mario is
        touching_ground - if mario is touching the ground
        touching_stairs - if mario is touching the stairs
        
    Methods:
        move - recives an imput and moves mario in the x axis accordingly, using the movement animation. 
        It also makes mario go upwards when needed
        moveVertical - recives an input and moves mario in the y axis accordingly when on a stair
        fall - makes mario constantly moves downwards unless its touching the ground (its nullified while jumping)
        jump - moves mario upwards during a certain time
        ground - detects if mario is touching the ground by comparing its positions
        level_check - changes the level of mario accordingly with its position
        stairs_check - checks if mario is touching the stairs by comparing its positions
        get_info - returns the overall information of mario
        position_reset - returns mario to its original position
        @Property methods - return an attribute of mario
    '''
    __xpos = 0
    __ypos = 0
    __originalx = 0
    __originaly = 0
    __w = 16
    __h = 16
    __sprite = 0
    __direction = 0
    __jump_interval = 0
    __level_ground = 0
    __touching_ground = False
    __touching_stairs = False
    
    def __init__(self,x,y):
        self.__xpos = x
        self.__ypos = y
        self.__originalx = x
        self.__originaly = y
        self.__sprite
        self.__jumping = 0

        
    def move(self, x):
        if self.__xpos <= 0 and x < 0:
            x = 0
        elif self.__xpos + self.__w >= constants.WIDTH and x > 0:
            x = 0
        elif self.__xpos + self.__w >= 187 and self.__ypos + self.__h in range(239, 255) and x > 0:
            x = 0
            
        
        self.__xpos += x
        if x > 0:
            self.__direction = 1
        elif x < 0:
            self.__direction = 0
           
        if self.__sprite in (3, 4):
            self.__sprite = 0
            
        con = True
        if self.__sprite == 0 and con:
            self.__sprite = 1
            con = False
        if self.__sprite == 1 and con:
            self.__sprite = 2
            con = False
        elif self.__sprite == 2 and con:
            self.__sprite = 0
            con = False
            
    def moveVertical(self, y):
        self.__ypos += y
        if self.__sprite not in (3, 4):
            self.__sprite = 3
            
        if self.__sprite == 3:
            self.__sprite = 4
        elif self.__sprite == 4:
            self.__sprite = 3

    
    def fall(self):
        if self.__ypos < constants.HEIGHT - 20 and self.__touching_ground  == False and not self.__touching_stairs:
            self.__ypos += 3
        else:
            self.__ypos = self.__ypos
            self.__jump_interval = 0

            
            
    def jump(self):
        self.__jump_interval += 1.5
        self.__ypos -= 7
        
    def ground(self, y):
        
        if self.__ypos >= y - 18 and self.__ypos < y - 10:
            self.__touching_ground = True
        else: 
            self.__touching_ground = False
            
    def level_check(self):
        if self.__ypos > constants.HEIGHT - 61:
            self.__level_ground = 0
        elif self.__ypos > constants.HEIGHT - 115 and self.__ypos <= constants.HEIGHT - 61:
            self.__level_ground = 1
        elif self.__ypos > constants.HEIGHT - 156 and self.__ypos <= constants.HEIGHT - 115:
            self.__level_ground = 2
        elif self.__ypos > constants.HEIGHT - 205 and self.__ypos <= constants.HEIGHT - 156:
            self.__level_ground = 3
        elif self.__ypos > constants.HEIGHT - 243 and self.__ypos <= constants.HEIGHT - 205:
            self.__level_ground = 4
        else:
            self.__level_ground = 5
        
        
    def stairs_check(self):
        stair = False
        up = False
        down = False
        

        if self.__ypos + self.__h in range(201 , 238) and self.__xpos in range(24, 40):
            stair = True
            if self.__ypos + self.__h in range(203 , 238):
                up = True
            if self.__ypos + self.__h in range(201, 238):
                down = True
        
        elif self.__ypos + self.__h in range(153, 193) and self.__xpos in range(146, 162): # 2nd stair
            stair = True
            if self.__ypos + self.__h in range(157, 192):
                up = True
            if self.__ypos + self.__h in range(153, 193):
                down = True
                
        elif self.__ypos + self.__h in range(103, 149) and self.__xpos in range(52, 68): # 3rd stair
            stair = True
            if self.__ypos + self.__h in range(107, 148):
                up = True
            if self.__ypos + self.__h in range(103, 149):
                down = True
                
        elif self.__ypos + self.__h in range(61, 99) and self.__xpos in range(143, 159): # 4th stair
            stair = True
            if self.__ypos + self.__h in range(62, 99):
                up = True
            if self.__ypos + self.__h in range(61, 99):
                down = True
        elif self.__ypos + self.__h in range(23, 59) and self.__xpos in range(104, 120): # 5th stair
            stair = True
            if self.__ypos + self.__h in range(26, 54):
                up = True
            if self.__ypos + self.__h in range(23, 59):
                down = True
        

        self.__touching_stairs =  stair
        return  stair, up, down
        
    def up_mario(self):
        if self.touching_ground == True:
            self.__ypos -= 1
   
    #--------------------------------------------------------
    
    def getInfo(self):
        return self.__xpos, self.__ypos, self.__w, self.__h
    
    @property
    def xpos(self):
        return self.__xpos
    
    @property
    def ypos(self):
        return self.__ypos
    
    @property
    def sprite(self):
        return self.__sprite
    
    @property
    def touching_ground(self):
        return self.__touching_ground
    
    @property
    def jump_interval(self):
        return self.__jump_interval  
    
    @property
    def direction(self):
        return self.__direction 
    
    @property
    def level(self):
        return self.__level_ground 
    
    def position_reset(self):
        self.__xpos = self.__originalx
        self.__ypos = self.__originaly

    def get_Frame(self):
        stairsInfo = self.stairs_check()
        if stairsInfo[0] == True: # Checks whether Mario is in a stair
            if self.sprite == 3:
                return (self.xpos, self.ypos, 0, 78, 32, 16, 16)
            elif self.sprite == 4: 
                return (self.xpos, self.ypos, 0, 101, 32, 16, 16)
            else:
                return (self.xpos, self.ypos, 0, 148, 32, 16, 16)
                
        else:
            if self.direction == 0:
                if self.sprite == 0:
                    return (self.xpos, self.ypos, 0, 6, 32, 16, 16)
                elif self.sprite == 1:
                    return (self.xpos, self.ypos, 0, 29, 32, 16, 16)
                elif self.sprite == 2:
                    return (self.xpos, self.ypos, 0, 53, 32, 16, 16)
                else:
                    return (self.xpos, self.ypos, 0, 148, 32, 16, 16)
            elif self.direction == 1:
                if self.sprite == 0:
                    return (self.xpos, self.ypos, 0, 192, 0, 16, 16)
                elif self.sprite == 1:
                    return (self.xpos, self.ypos, 0, 208, 0, 16, 16)
                elif self.sprite == 2:
                    return (self.xpos, self.ypos, 0, 224, 0, 16, 16)
                else:
                    return (self.xpos, self.ypos, 0, 148, 32, 16, 16)
        