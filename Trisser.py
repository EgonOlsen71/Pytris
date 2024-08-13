import random
from Block import Block
from ArrayRenderer import ArrayRenderer
from PixelRenderer import PixelRenderer
from GameState import GameState

#   @author EgonOlsen71
#
class Trisser:
    
    def __init__(self, screen):
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
        self.pixeler.renderScore(self.score)
        self.state = GameState.RUNNING

    def removeLines(self, field):
        maxX = len(field)
        maxY = len(field[0])
        modified = False
        scoreMul = 1
        for y in range(0, maxY):
            val = 0
            for x in range(0, maxX):
                val += 1 if field[x][y] else 0
            if val==maxX:
                for y2 in range(y-1, 0, -1):
                    for x2 in range(0, maxX):
                        field[x2][y2+1] = field[x2][y2]
                        modified = True
                self.score += 100*scoreMul
                scoreMul+=1
        return modified


    def hasEnded(self):
        return GameState.GAME_OVER==self.state

    def process(self=False, left=False, right=False, up=False, dropDown=False):
        if self.state == GameState.GAME_OVER:
            self.pixeler.renderGameOver()
            return
        
        if self.currentBlock==None:
            index = random.randint(0, len(self.blueprints)-1)
            self.currentBlock = self.blueprints[index].clone()
            moved = self.currentBlock.move(self.renderer.field, 0, 0)
            if not moved:
                self.currentBlock = None
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
                modified = self.removeLines(self.renderer.field)
                self.currentBlock = None
                if modified:
                    self.pixeler.renderField(self.renderer.field)
                    self.pixeler.renderScore(self.score)
            