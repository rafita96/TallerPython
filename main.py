import pygame, os
from pygame.locals import *
import menu, funciones,random
# No tocar
pygame.init()

screen = pygame.display.set_mode((640,480))
font = pygame.font.Font(os.path.join("data","maiden.TTF"),50)
siguiente = menu.menu(screen, font)

if not siguiente:
    exit()
# fin de no tocar

# El usuario define su lista de palabras
lista = ["hola", "perro"]

palabra = random.choice(lista)
errores = 0

while True:
    letra = funciones.obtenerLetra(pygame)
    if letra == "":
        continue

    print(letra)