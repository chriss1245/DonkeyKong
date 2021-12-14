from game import Game
import constants    
import pyxel


class Controller:
    '''
    The controller of the game. constains the different windows of the whole game
    Methods:
        start - resets the game each time the user wants to play
        draw - draws the frames
        update - updates the objects and the state of the game
    '''
    
    #Initial preparations
    # [menu,  playing , lost, won]
    def __init__(self):
        self.state = 'menu'
        self.game = Game(pyxel)
        pyxel.run(self.update, self.draw)
    #------------------------------------------------------------------------------
    def start(self):
        self.game.start(pyxel)

    def update(self):
        frames = pyxel.frame_count

        if self.state == 'menu' or self.state == 'lost' or self.state == 'won': # Interface of the seccondary windows
                self.game.update(pyxel)
                if pyxel.btnp(pyxel.KEY_RETURN):
                    self.start()
                    self.state = 'playing'
                if pyxel.btnp(pyxel.KEY_Q):
                    pyxel.quit()
        
        elif self.state == 'playing':
            self.state = self.game.update(pyxel)
        
 
    #----------------------------------------------------------------------------
    def draw(self):
        if self.state == 'menu': # menu window
            # Text
            pyxel.cls(0)
            if pyxel.frame_count % 100 < 25:
                pyxel.blt(0, 0, 2, 250, 0, 0, 0)
            elif pyxel.frame_count % 100 < 50:
                pyxel.blt(25, 41, 2, 56, 0, 52, 15)
            elif pyxel.frame_count % 100 < 75:
                pyxel.blt(25, 41, 2, 56, 0, 80, 15)
            else:
                pyxel.blt(25, 41, 2, 56, 0, 150, 15)
                
            if pyxel.frame_count % 50 < 25:
                pyxel.blt(60, 225, 2, 56, 70, 80, 8)
            
            pyxel.blt(70, 240, 2, 56, 85, 80, 8)
            
            # Animation
            if (pyxel.frame_count // 2) % 2 == 0: # Mario
                pyxel.blt((pyxel.frame_count - 10) % (constants.WIDTH + 12), 150, 0, 208, 0, 16, 16)
            else:
                pyxel.blt((pyxel.frame_count - 10) % (constants.WIDTH + 12), 150, 0, 224, 0, 16, 16)
            
            # Barrels
            if (pyxel.frame_count // 2) % 4 == 0:
                pyxel.blt((pyxel.frame_count - 50) % (constants.WIDTH + 12), 156, 0, 35, 106, 12, 10)
            elif (pyxel.frame_count // 2) % 4 == 1:
                pyxel.blt((pyxel.frame_count - 50) % (constants.WIDTH + 12), 156, 0, 59, 106, 12, 10)
            elif (pyxel.frame_count // 3) % 4 == 2:
                pyxel.blt((pyxel.frame_count - 50) % (constants.WIDTH + 12), 156, 0, 83, 106, 12, 10)
            else:
                pyxel.blt((pyxel.frame_count - 50) % (constants.WIDTH + 12), 156, 0, 107, 106, 12, 10)
                
                
        elif self.state == 'lost':  # Lost window
            pyxel.cls(0)
            pyxel.blt(25, 41, 2, 56, 20, 150, 23) # Game over
            
            # Pauline and the hart
            pyxel.blt(80, 130, 2, 49, 193, 16, 23) 
            pyxel.blt(60, 120, 0, 214, 180, 16, 12)
            
            if pyxel.frame_count % 50 < 25: # Press enter to play again
                pyxel.blt(60, 225, 2, 56, 70, 80, 8)
            
            pyxel.blt(70, 240, 2, 56, 85, 80, 8) # Press q to quit
            
            
        elif self.state == 'won': # Won window
            pyxel.cls(0)
            pyxel.blt(45, 41, 2, 56, 45, 155, 23)  # You won
            
            # Pauline and hearts animation
            pyxel.blt(80, 130, 2, 49, 193, 16, 23) 
            if (pyxel.frame_count + 5) % 50 < 25:
                pyxel.blt(60, 120, 0, 191, 180, 15, 12)
            else:
                pyxel.blt(100, 120, 0, 191, 180, 15, 12)
            
            if pyxel.frame_count % 50 < 25: # Press enter to play again
                pyxel.blt(60, 225, 2, 56, 70, 80, 8)
            
            pyxel.blt(70, 240, 2, 56, 85, 80, 8) # Press q to quit
            
        elif self.state == 'playing':
            self.game.draw(pyxel)
## main      
Controller()