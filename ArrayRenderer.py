from AbstractRenderer import AbstractRenderer

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
            self.field[element[0]][element[1]]=True if plot else None
