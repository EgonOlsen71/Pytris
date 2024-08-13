import copy
import pygame

#   @author EgonOlsen71
#
class Block():

    def __init__(self, second, third, forth, rotatable=True):
        self.offsets=[(0,0), second, third, forth]
        self.xPosition=3
        self.yPosition=1
        self.rotation=0
        self.rotatable = rotatable
        self.color = pygame.Color(255,255,255)
       

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
        return xMul * element[1] + yMul * element[0]

    def checkForObstacle(self, xPos, yPos, field):
        if xPos<0 or xPos>=len(field):
            return True
        if yPos<0 or yPos>=len(field[0]):
            return True
        if field[xPos][yPos]!=None:
            return True
        return False

    def move(self, field, xAdd, yAdd):
        xPos = self.xPosition + xAdd
        yPos = self.yPosition + yAdd
        xMul, yMul = self.getRotationValues(self.rotation)

        for element in self.offsets:
            xPos +=self.getXPosition(xMul, yMul, element)
            yPos +=self.getYPosition(xMul, yMul, element)
            if self.checkForObstacle(xPos, yPos, field):
                return False
            
        self.xPosition += xAdd
        self.yPosition += yAdd
        return True

    def rotate(self, field):
        if not self.rotatable:
            return False
        xPos = self.xPosition
        yPos = self.yPosition
        rot = self.rotation
        rot +=1
        if rot > 3:
            rot = 0
        
        xMul, yMul = self.getRotationValues(rot)

        for element in self.offsets:
            xPos +=self.getXPosition(xMul, yMul, element)
            yPos +=self.getYPosition(xMul, yMul, element)
            if self.checkForObstacle(xPos, yPos, field):
                return False
            
        self.rotation = rot
        return True

