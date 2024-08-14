import pygame

#   A simple sound player
#   @author EgonOlsen71
#

class SoundPlayer:

    def __init__(self):
        self.drop = pygame.mixer.Sound("sounds/drop.ogg")
        self.gameOver = pygame.mixer.Sound("sounds/game_over.wav")
        self.rumble = pygame.mixer.Sound("sounds/rocks.wav")
        self.start = pygame.mixer.Sound("sounds/game-start.ogg")
    
    def playDropSound(self):
        self.drop.set_volume(0.5)
        self.drop.play()
        
    def playGameOverSound(self):
        self.gameOver.set_volume(1)
        self.gameOver.play()
        
    def playRumbleSound(self):
        self.rumble.set_volume(0.5)
        self.rumble.play()
        
    def playStartSound(self):
        self.start.set_volume(1)
        self.start.play()