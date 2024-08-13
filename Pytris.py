import pygame
from Trisser import Trisser

#   @author EgonOlsen71
#

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pytris")
clock = pygame.time.Clock()

pygame.mouse.set_visible(True)
pygame.event.set_grab(False)

running = True
game = Trisser(screen)
speed = 10
cnt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        running = False
    if pressed[pygame.K_DOWN] and cnt<speed / 2:
        cnt = speed / 2

    cnt+=1
    if cnt>speed:
        cnt=0
        game.process(pressed[pygame.K_LEFT], pressed[pygame.K_RIGHT], pressed[pygame.K_UP], pressed[pygame.K_DOWN])   
        pygame.display.flip()

    clock.tick(60) 

pygame.quit()