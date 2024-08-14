from AbstractRenderer import AbstractRenderer

#   Renderer implementation that renders a block into a playfield array.
#   @author EgonOlsen71
#
class ArrayRenderer(AbstractRenderer):

    def __init__(self, width, height):
        self.field = [[None for _ in range(height)] for _ in range(width)]
        
    def render(self, block):
        self.internalRender(block)

    def derender(self, block):
        self.internalRender(block, False)

    def internalRender(self, block, plot=True):
        pos = block.getAbsolutePositions()
        for element in pos:
            self.field[element[0]][element[1]]=block.color if plot else None

    def removeLines(self):
        maxX = len(self.field)
        maxY = len(self.field[0])
        score = 0
        scoreMul = 1
        for y in range(0, maxY):
            val = 0
            for x in range(0, maxX):
                val += 1 if self.field[x][y] else 0
            if val==maxX:
                for x2 in range(maxX):
                    self.field[x2][1:y+1] = self.field[x2][0:y]
                    self.field[x2][0] = None    
                score += 100*scoreMul
                scoreMul+=1
        return score
