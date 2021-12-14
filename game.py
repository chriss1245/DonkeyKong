from mario import mario
from suelo import suelo
from stair import stair
from donkey import Donkey
from paulone import Paulone
from barril import Barril
from lifes import lifes
from score import points
import constants

x = constants.X
y = constants.Y
initial_x = constants.MARIO_X
initial_y = constants.MARIO_Y

class Game:
    '''
    The class representing the player character (Mario)
    Attributes:
        state - indicates which window shuld the program show
        
    Methods:
        start - resets the game each time the user wants to play
        draw - draws the frames
        update - updates the objects and the state of the game
    '''
    
    #Initial preparations
     #[0, 1, 2, 3, 4] # [Menu, Beginig, Playing , Game over, Won]
    def __init__(self, pyxel):
 
        #Creating the loose condition
        self.state = 'menu'
        pyxel.init(constants.WIDTH, constants.HEIGHT)
        pyxel.load(r'assets/mario.pyxres')
        pyxel.image(2).load(56, 0, "assets/Mario-vs-Donkey.png")
        pyxel.image(2).load(56, 20, "assets/Game-Over.png")
        pyxel.image(2).load(56, 45, "assets/You-won.png")
        pyxel.image(2).load(56, 70, "assets/enter.png")
        pyxel.image(2).load(56, 85, "assets/Press-Q-to-quit.png")
        pyxel.image(2).load(56, 110, "assets/play_again.png")
        self.start(pyxel)

    #------------------------------------------------------------------------------
    def start(self, pyxel):
        #Creating the Music
        pyxel.playm(0, loop = True)
        
        # Creating the Characters
        self.donkey = Donkey()
        self.player = mario(initial_x, initial_y)
        self.pauli = Paulone()
        # Creating the barrils
        self.barrels = []
        #Creating the score and lives system
        self.lifes = lifes(50,5)
        self.score = points(0, 2)
        
        #Creation of the Ground
        #----------------------------------------------------------------------
        self.grounds = []
        level = []
        elevation = 0
        for i in range(1, constants.WIDTH, 8):
            level.append(suelo(i, constants.HEIGHT - 8 - 8 - elevation//3, 0))
            if i < constants.WIDTH// 1.5:
                elevation -= 1
        self.grounds.append(level)
        
        level = []
        elevation = 0
        for i in range(24, constants.WIDTH, 8):
            level.append(suelo(i, constants.HEIGHT - 46 - 8 - elevation//3, 1))
            elevation += 1
        self.grounds.append(level)
        
        level = []    
        elevation = 0
        for i in range(0, constants.WIDTH - 24, 8):
            level.append(suelo(i, constants.HEIGHT - 98- 8 - elevation//3, 2))
            elevation -= 1
        self.grounds.append(level)
        
        level = []
        elevation = 0
        for i in range(24, constants.WIDTH, 8):
            level.append(suelo(i, constants.HEIGHT - 140 - 8 - elevation//3, 3))
            elevation += 1
        self.grounds.append(level)
        
        level = []    
        elevation = 0
        for i in range(1, constants.WIDTH - 36, 8):   
            level.append(suelo(i, 58 - elevation//3, 4))
            if i > (constants.WIDTH // 2.5): 
                elevation -= 1
        self.grounds.append(level)
        
        level = []  
        elevation = 0
        for i in range(constants.WIDTH//2, constants.WIDTH, 8):
            level.append(suelo(i, 25 - elevation, 5))
        self.grounds.append(level)
        #----------------------------------------------------------------------
        
        #Creation of the Stairs
        #----------------------------------------------------------------------
        self.stairs = []
        row = []
        for i in range(constants.HEIGHT - 20, constants.HEIGHT - 62, -6 ):
            row.append(stair(36,i))
     
        self.stairs.append(row)
        
        row = []
        for i in range(constants.HEIGHT- 63, constants.HEIGHT - 105, -6 ):
            row.append(stair(constants.WIDTH - 42,i -2))
        self.stairs.append(row)
        
        row = []
        for i in range(constants.HEIGHT - 110, constants.HEIGHT - 156, -6 ):
            row.append(stair(64,i + 1))
  
        self.stairs.append(row)
        
        row = []
        for i in range(constants.HEIGHT- 157, constants.HEIGHT - 199, -6 ):
            row.append(stair(constants.WIDTH - 48,i -2))
        self.stairs.append(row)
        
        row = []
        for i in range(constants.HEIGHT- 199, constants.HEIGHT - 235, -6 ):
            row.append(stair(constants.WIDTH - 84,i -2))
        self.stairs.append(row)
        #----------------------------------------------------------------------
        
    def update(self, pyxel):
        frames = pyxel.frame_count
        #Ground
        self.player.level_check()
        con = False   
    
            #To check if thereis ground under
        for levels in self.grounds:
            for i in levels:
            # print(i.xpos-8 <= self.player.xpos ,i.xpos + 8 >= self.player.xpos ,self.player.level == i.level ,con == False)
                if i.xpos - 8 <= self.player.xpos and i.xpos + 8 >= self.player.xpos and self.player.level == i.level and con == False:
                    self.player.ground(i.ypos)
                    con = True
                elif con == False:
                    self.player.ground(0)
        
        
        #Mario movement
        self.player.fall()
    
        stairsInfo = self.player.stairs_check() # (is there stairs?, can i go up?, can i go down?)
    
        if pyxel.btn(pyxel.KEY_UP):
            if stairsInfo[0] == True:
                if stairsInfo[1] == True:
                    self.player.moveVertical(-y)
                else:
                    self.player.jump()
            else:
                if self.player.jump_interval <= 6: # it was 10
                    self.player.jump()
    
        if pyxel.btn(pyxel.KEY_DOWN):
            if stairsInfo[0] == True:
                if stairsInfo[2] == True:
                    self.player.moveVertical(y)
            
        if pyxel.btn(pyxel.KEY_LEFT):
            if stairsInfo[0] == False or (stairsInfo[1] == False or stairsInfo[2] == False):
                self.player.move(-x)
                self.player.up_mario()
        if pyxel.btn(pyxel.KEY_RIGHT):
            if stairsInfo[0] == False or (stairsInfo[1] == False or stairsInfo[2] == False):
                self.player.move(x)
                self.player.up_mario()
        
        #Pauline
        self.pauli.update(frames)
        
        # Donkey barrils
        throwBarril = self.donkey.update(frames) # Returns true if the sprites were compleated
    
        # Barrels 
        if len(self.barrels) > 0:
            for _ in range(len(self.barrels)):
                if self.barrels[0].ypos >220  and self.barrels[0].xpos > 180- 8: 
                    self.barrels.remove(self.barrels[0])
                
        if throwBarril:
            if len(self.barrels) < 10:
                self.barrels.append(Barril(56, 45))
    
        for b in self.barrels:
            b.update(frames)
        
        #Check if mario is touching a barrel
        for i in self.barrels:
            if self.player.xpos > i.xpos - 8 and self.player.xpos < i.xpos + 8 and self.player.ypos > i.ypos - 8 and self.player.ypos < i.ypos + 10:
                if self.player.xpos + 16 not in range(180, 200) or self.player.ypos + 16 not in range(229, 255):
                    self.lifes.dmg()
                    self.player.position_reset()
                    self.score.scorereset()
        
            
        #Check if Mario Jumps over a barrel 
        for i in self.barrels:
            if self.player.xpos > i.xpos - 10 and self.player.xpos < i.xpos + 10  and self.player.ypos < i.ypos and self.player.ypos > i.ypos - 25:
                self.score.scorespoint(200)

        # Checks if mario have not lost or won yet.
        if self.lifes.lives == 0:
            return 'lost'
        if self.player.level == 5 and self.player.xpos in range(129, 150):
            return 'won'
        
        return 'playing'
 
    #----------------------------------------------------------------------------
    def draw(self, pyxel):
        # Refresh
        pyxel.cls(0)
        
            # Drows the stairs
        for element in self.stairs:
            for i in element:
                pyxel.blt(i.xpos, i.ypos, 0, 0, 18, 8, 6)    
        
        #Mario movement
        pyxel.blt(*self.player.get_Frame())

        #Ground 
        for level in self.grounds:
            for i in level:
                pyxel.blt(i.xpos, i.ypos, 0, 0, 8, 8 , 8)
                    
        #Lifes and Points
        lifes = self.lifes.getFrames() # Saves a list containing tree tuples, one for each heart
        for life in lifes:
            pyxel.blt(*life) # drawing the heart
        
        pyxel.blt(self.score.xpos, self.score.ypos, 0, 181, 100, 43, 19)
        s = str(self.score.score)
        pyxel.text(self.score.xpos + 6, self.score.ypos + 10, s, 7)
        
        
        # Donkey animation
        pyxel.blt(*self.donkey.getFrame())
        
        # Barrels animation
        for barrel in self.barrels: 
            pyxel.blt(*barrel.getFrame())
        
        # Paulone
        pyxel.blt(*self.pauli.getFrame())
        
        if self.pauli.xpos <= 140:
            pyxel.blt(113, 1, 0, 126, 182, 22, 7)
        elif self.pauli.xpos >= 172:
            pyxel.blt(150, 1, 0, 126, 182, 22, 7)
        
        # Barril of the left at the bootom
        pyxel.blt(185, 230, 0, 8, 0, 15, 15)
        
        if pyxel.frame_count // 4 % 4 == 0:
            pyxel.blt(185, 215, 0, 24, 1, 15, 15)
        elif pyxel.frame_count // 4 % 4 == 1:
            pyxel.blt(185, 215, 0, 40, 1, 15, 15)
        elif pyxel.frame_count // 4 % 4 == 2:
            pyxel.blt(185, 215, 0, 56, 0, 15, 15)
        else:
            pyxel.blt(185, 215, 0, 72, 0, 15, 15)
    
        # Static barrils
        pyxel.blt(5, 25, 0, 12, 103, 10, 16)
        pyxel.blt(16, 25, 0, 12, 103, 10, 16)
        pyxel.blt(5, 41, 0, 12, 103, 10, 16)
        pyxel.blt(16, 41, 0, 12, 103, 10, 16)  