import copy
import pygame

#   @author EgonOlsen71
#
class Block():

    def __init__(self, first, second, third, forth, color, rotatable=True):
        self.offsets=[first, second, third, forth]
        self.xPosition=4
        self.yPosition=1
        self.rotation=0
        self.rotatable = rotatable
        match color:
            case 0:
                self.color = pygame.Color(255,255,255)
            case 1:
                self.color = pygame.Color(255,0,0)
            case 2:
                self.color = pygame.Color(0,255,0)    
            case 3:
                self.color = pygame.Color(0,0,255) 
            case 4:
                self.color = pygame.Color(255,255,0)
            case 5:
                self.color = pygame.Color(255,0,255)
            case 6:
                self.color = pygame.Color(0,255,255)

    def clone(self):
        return copy.deepcopy(self)
    
    def getRotationValues(self, rot):
        match rot:
            case 1:
                yMul = 1
                xMul = 0
            case 2:
                yMul = 0
                xMul = -1
            case 3:
                yMul = -1
                xMul = 0
            case _:
                yMul = 0
                xMul = 1
        return xMul, yMul

    def getAbsolutePositions(self):
        xPos = self.xPosition
        yPos = self.yPosition
        xMul, yMul = self.getRotationValues(self.rotation)

        ret = []

        for element in self.offsets:
            xPos +=self.getXPosition(xMul, yMul, element)
            yPos +=self.getYPosition(xMul, yMul, element)
            ret.append((xPos, yPos))
        return ret

    def getXPosition(self, xMul, yMul, element):
        return xMul * element[0] + yMul * element[1]
    
    def getYPosition(self, xMul, yMul, element):
        return xMul * element[1] - yMul * element[0]

    def checkForObstacle(self, xPos, yPos, field):
        if xPos<0 or xPos>=len(field):
            return True
        if yPos<0 or yPos>=len(field[0]):
            return True
        if field[xPos][yPos]!=None:
            return True
        return False

    def canBePlaced(self, xPos, yPos, xMul, yMul, field):
        for element in self.offsets:
            xPos +=self.getXPosition(xMul, yMul, element)
            yPos +=self.getYPosition(xMul, yMul, element)
            if self.checkForObstacle(xPos, yPos, field):
                return False
        return True

    def move(self, field, xAdd, yAdd):
        xPos = self.xPosition + xAdd
        yPos = self.yPosition + yAdd
        xMul, yMul = self.getRotationValues(self.rotation)
        ok = self.canBePlaced(xPos, yPos, xMul, yMul, field)
       
        if ok:    
            self.xPosition += xAdd
            self.yPosition += yAdd
        return ok

    def rotate(self, field):
        if not self.rotatable:
            return False
        xPos = self.xPosition
        yPos = self.yPosition
        rot = self.rotation-1
        if rot < 0:
            rot = 3
        
        xMul, yMul = self.getRotationValues(rot)
        ok = self.canBePlaced(xPos, yPos, xMul, yMul, field)
        
        if ok:
            self.rotation = rot
        return ok

