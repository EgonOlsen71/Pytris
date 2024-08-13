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
rotCnt = 0
left = right = up = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        running = False
    if pressed[pygame.K_DOWN] and cnt<speed // 2:
        cnt = speed // 2 

    left = left | pressed[pygame.K_LEFT]
    right = right | pressed[pygame.K_RIGHT]
    up = up | pressed[pygame.K_UP]

    if left and right:
        right = False

    rotCnt +=1
    if rotCnt <= 8:
        left = right = up = False

    cnt+=1
    if cnt>speed or left or right or up:
        game.process(left, right, up, cnt>speed)   
        left = right = up = False
        
        pygame.display.flip()
        if cnt>speed:
            cnt = 0
        if rotCnt>8:
            rotCnt = 0

    clock.tick(60) 

pygame.quit()