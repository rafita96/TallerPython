import pygame
from pygame.locals import *
import inicio
# No tocar
pygame.init()

screen = pygame.display.set_mode((640,480))
jugar = inicio.menu(screen)

if not jugar:
    exit()
# No tocar


