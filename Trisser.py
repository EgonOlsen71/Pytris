import random
from Block import Block
from ArrayRenderer import ArrayRenderer
from PixelRenderer import PixelRenderer
from GameState import GameState

#   The main game class
#   @author EgonOlsen71
#
class Trisser:

    def __init__(self, screen, sounds):
        self.blueprints = (Block((-1,0), (1,0), (1,0), (1,0) , 0), 
                           Block((-1,0), (0,-1), (1,1), (1,0), 1), 
                           Block((-1,0), (1,0), (1,0), (0,-1), 2),
                           Block((0,0), (1,0), (0,-1), (-1,0), 3, False),
                           Block((-1,0), (1,0), (0,-1), (1,0), 4),
                           Block((-1,0), (1,0), (0,-1), (1,1), 5),
                           Block((-1,-1), (1,0), (0,1), (1,0), 6))
        
        self.renderer = ArrayRenderer(10, 23)
        self.pixeler = PixelRenderer(screen, 24, 100, 20, 10, 23)
        self.currentBlock = None
        self.score = 0
        self.state = GameState.INITIAL
        self.sounds = sounds

    def getSpeed(self):
        return max(4, 25-self.score//1500)

    def hasEnded(self):
        return GameState.GAME_OVER==self.state
    
    def startGame(self):
        self.state = GameState.RUNNING
        self.pixeler.renderBackdrop()
        self.pixeler.renderScore(self.score)
        self.sounds.playStartSound()

    def isInitial(self):
        return GameState.INITIAL==self.state

    def process(self=False, left=False, right=False, up=False, dropDown=False):
        if self.state == GameState.GAME_OVER:
            self.pixeler.renderGameOver()
            return
        
        if self.state == GameState.INITIAL:
            self.pixeler.renderIntro()
            return
        
        if self.currentBlock==None:
            index = random.randint(0, len(self.blueprints)-1)
            self.currentBlock = self.blueprints[index].clone()
            moved = self.currentBlock.move(self.renderer.field, 0, 0)
            if not moved:
                self.currentBlock = None
                if self.state != GameState.GAME_OVER:
                    self.sounds.playGameOverSound()
                self.state = GameState.GAME_OVER
        else:
            self.renderer.derender(self.currentBlock)
            self.pixeler.derender(self.currentBlock)

            move = 0
            if left:
                move = -1
            elif right:
                move = 1

            if move != 0:
                self.currentBlock.move(self.renderer.field, move, 0)
            if up:
                self.currentBlock.rotate(self.renderer.field)

            if dropDown:
                moved = self.currentBlock.move(self.renderer.field, 0, 1)
            self.renderer.render(self.currentBlock)
            self.pixeler.render(self.currentBlock)
            if dropDown and not moved:
                self.sounds.playDropSound()
                tmpScore = self.renderer.removeLines()
                self.score += tmpScore
                modified = tmpScore>0
                self.currentBlock = None
                if modified:
                    self.sounds.playRumbleSound()
                    self.pixeler.renderField(self.renderer.field)
                    self.pixeler.renderScore(self.score)
            