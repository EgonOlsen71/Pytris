from AbstractRenderer import AbstractRenderer
import pygame

#   @author EgonOlsen71
#
class PixelRenderer(AbstractRenderer):

    def __init__(self, screen, blockSize, offsetX, offsetY, width, height):
        self.blockSize = blockSize
        self.screen = screen
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.width = width
        self.height = height
        self.black = pygame.Color(0,0,0)
        self.white = pygame.Color(255,255,255)

    def render(self, block):
        self.internalRender(block)

    def derender(self, block):
        self.internalRender(block, False)

    def internalRender(self, block, plot=True):
        self.drawDecorations()
        pos = block.getAbsolutePositions()
        color = block.color if plot else self.black
        for element in pos:
            xPos = element[0]*self.blockSize + self.offsetX
            yPos = element[1]*self.blockSize + self.offsetY
            pygame.Surface.fill(self.screen, color, pygame.Rect(xPos, yPos, self.blockSize, self.blockSize))

    def renderField(self, field):
        maxX = len(field)
        maxY = len(field[0])
        yPos = self.offsetY
        for y in range(0, maxY):
            xPos = self.offsetX
            for x in range(0, maxX):
                color = field[x][y]
                if color == None:
                    color = self.black
                pygame.Surface.fill(self.screen, color, pygame.Rect(xPos, yPos, self.blockSize, self.blockSize))
                xPos += self.blockSize
            yPos += self.blockSize

    def drawDecorations(self):
        pygame.draw.rect(self.screen, self.white, pygame.Rect(self.offsetX-2, self.offsetY-2, self.blockSize*self.width+4, self.blockSize*self.height+4), 1)
