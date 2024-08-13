import random
from Block import Block
from ArrayRenderer import ArrayRenderer
from PixelRenderer import PixelRenderer

#   @author EgonOlsen71
#
class Trisser:
    
    def __init__(self, screen):
        self.blueprints = (Block((1,0), (1,0), (1,0)), Block((0,-1), (1,1), (1,0)), Block((1,0), (1,0), (0,-1)),
                           Block((1,0), (0,-1), (-1,0), False),Block((1,0), (0,-1), (1,0)),Block((1,0), (0,-1), (1,1)),
                           Block((1,0), (0,1), (1,0)))
        self.renderer = ArrayRenderer(10, 23)
        self.pixeler = PixelRenderer(20, screen, 100, 20, 10, 23)
        self.currentBlock = None

    def process(self, left, right, up, down):
        if self.currentBlock==None:
            index = random.randint(0, len(self.blueprints)-1)
            self.currentBlock = self.blueprints[index].clone()
            moved = self.currentBlock.move(self.renderer.field, 0, 0)
            if not moved:
                self.currentBlock = None
                # todo handle end game...
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

            moved = self.currentBlock.move(self.renderer.field, 0, 1)
            self.renderer.render(self.currentBlock)
            self.pixeler.render(self.currentBlock)
            if not moved:
                self.currentBlock = None
            