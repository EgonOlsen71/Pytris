import pygame
import time
from Trisser import Trisser
from SoundPlayer import SoundPlayer

#   @author EgonOlsen71
#

pygame.init()
sounds = SoundPlayer()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pytris")
clock = pygame.time.Clock()

pygame.mouse.set_visible(True)
pygame.event.set_grab(False)

running = True
game = None
speed = cnt = rotCnt = 0
left = right = up = False 


def init():
    global speed, cnt, rotCnt, left, right, up, game
    game = Trisser(screen, sounds)
    speed = game.getSpeed()
    cnt = 0
    rotCnt = 0
    left = right = up = False    

def waitingDone():
    game.process()
    pygame.display.flip()
    pygame.event.pump()
    pressy = pygame.key.get_pressed()
    return pressy[pygame.K_SPACE] or pressy[pygame.K_RETURN]

def waitForKeyReleased():
    while True:
        pygame.event.pump()
        pressy = pygame.key.get_pressed()
        if not (pressy[pygame.K_SPACE] or pressy[pygame.K_RETURN]):
            break
        time.sleep(0.16)

init()

while running:

    speed = game.getSpeed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        running = False

    if game.hasEnded():
        if waitingDone():
            waitForKeyReleased()
            init()
    elif game.isInitial():
       if waitingDone():
            waitForKeyReleased()
            game.startGame()
    else:
        if pressed[pygame.K_DOWN] and cnt<speed-2:
            cnt = max(2, speed-2)

        left = left or pressed[pygame.K_LEFT]
        right = right or pressed[pygame.K_RIGHT]
        up = up or pressed[pygame.K_UP]

        if left and right:
            right = False

        if not(left or right or up):
            rotCnt = 99

        rotCnt +=1
        if rotCnt <= 8:
            left = right = up = False

        cnt+=1
        if cnt>speed or left or right or up:
            game.process(left, right, up, cnt>speed)
            pygame.display.flip()   
            left = right = up = False
            
            if cnt>speed:
                cnt = 0
            if rotCnt > 8:
                rotCnt = 0

    clock.tick(60) 

pygame.quit()