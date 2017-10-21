import pygame
from pygame.locals import *

def menu(screen, font):
    image = pygame.Surface((50,50))
    image.fill((255,255,255))
    pygame.draw.polygon(image,(0,0,0),[(0,0),(0,50),(25,25)],5)

    pos = 1

    option1 = font.render("Iniciar",True,(0,0,0))
    option2 = font.render("Salir",True,(0,0,0))

    while True:
        screen.fill((255, 255, 255))
        screen.blit(option1,(200,100))
        screen.blit(option2,(200,200))
        screen.blit(image, (130, pos*100))
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_DOWN:
                    pos = 2
                elif e.key == K_UP:
                    pos = 1
                elif e.key == K_RETURN:
                    if pos == 1:
                        return True
                    elif pos == 2:
                        exit()
        pygame.display.update()