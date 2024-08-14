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
        self.dynColorDark = pygame.Color(0,0,0)
        self.dynColorLight = pygame.Color(0,0,0)
        self.black = pygame.Color(0,0,0)
        self.white = pygame.Color(255,255,255)
        self.red = pygame.Color(255,80,80)
        self.font = pygame.font.Font(None, 50)
        self.bigFont = pygame.font.Font(None, 130)
        self.bigFontOutline = pygame.font.Font(None, 132)
        self.screen.fill(self.black)
        self.backDrop = pygame.image.load("images/backdrop.png")
        self.renderBackdrop()
        
    def render(self, block):
        self.internalRender(block)

    def derender(self, block):
        self.internalRender(block, False)

    def renderBackdrop(self):
        self.screen.blit(self.backDrop, (0, 0))
        self.drawDecorations()
        pygame.Surface.fill(self.screen, self.black, pygame.Rect(self.offsetX-1, self.offsetY-1, self.blockSize*self.width+2, self.blockSize*self.height+2))

    def internalRender(self, block, plot=True):
        pos = block.getAbsolutePositions()
        color = block.color if plot else self.black
        for element in pos:
            xPos = element[0]*self.blockSize + self.offsetX
            yPos = element[1]*self.blockSize + self.offsetY
            self.renderBlock(xPos, yPos, color)

    def renderIntro(self):
        info = pygame.display.Info()
        width = info.current_w
        height = info.current_h
        texts = ("PYTRIS by EgonOlsen71", "CRSR to move/rotate/drop", "", "Press SPACE to start!")
        line = 0
        for text in texts:
            surface = self.font.render(text, True, self.white, self.black)
            rect = surface.get_rect()
            rect.topleft = (width/2-rect.centerx-1, height/3-rect.centery+line*35)
            line +=1
            self.screen.blit(surface, rect)

    def renderBlock(self, xPos, yPos, color):
        self.dynColorLight.update(int(min(255, color.r*1.3)), int(min(255, color.g*1.3)), int(min(255, color.b*1.3)))
        self.dynColorDark.update(int(min(255, color.r*0.7)), int(min(255, color.g*0.7)), int(min(255, color.b*0.7)))
        pygame.Surface.fill(self.screen, color, pygame.Rect(xPos+1, yPos+1, self.blockSize-2, self.blockSize-2))
        pygame.draw.lines(self.screen, self.dynColorLight, False, [(xPos, yPos+self.blockSize-1), (xPos, yPos),(xPos+self.blockSize-1, yPos)])
        pygame.draw.lines(self.screen, self.dynColorDark, False, [(xPos+self.blockSize-1, yPos), (xPos+self.blockSize-1, yPos+self.blockSize-1), (xPos, yPos+self.blockSize-1)])

    def renderGameOver(self):
        text = "GAME OVER!"
        info = pygame.display.Info()
        width = info.current_w
        height = info.current_h
        surface = self.bigFontOutline.render(text, True, self.white)
        rect = surface.get_rect()
        rect.topleft = (width/2-rect.centerx-1, height/2-rect.centery)
        self.screen.blit(surface, rect)

        surface = self.bigFont.render(text, True, self.red)
        rect = surface.get_rect()
        rect.topleft = (width/2-rect.centerx, height/2-rect.centery)
        self.screen.blit(surface, rect)

    def renderField(self, field):
        maxX = len(field)
        maxY = len(field[0])
        yPos = self.offsetY
        for y in range(0, maxY):
            xPos = self.offsetX
            for x in range(0, maxX):
                color = field[x][y]
                if not color:
                    color = self.black
                self.renderBlock(xPos, yPos, color)
                xPos += self.blockSize
            yPos += self.blockSize

    def renderScore(self, score):
        text = "Score: "+str(score)
        surface = self.font.render(text, True, self.white)
        rect = surface.get_rect()
        rect.topleft = (400, 20)
        fillRect = pygame.Rect(rect.topleft[0]-4, rect.topleft[1]-4, rect.width+8, rect.height+8)
        pygame.Surface.fill(self.screen, self.black, fillRect)
        self.screen.blit(surface, rect)

    def drawDecorations(self):
        pygame.draw.rect(self.screen, self.white, pygame.Rect(self.offsetX-2, self.offsetY-2, self.blockSize*self.width+4, self.blockSize*self.height+4), 1)

