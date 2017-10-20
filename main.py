import pygame, os
from pygame.locals import *
import menu, funciones,random
# No tocar
pygame.init()

pantalla = pygame.display.set_mode((640,480))
font_letra = pygame.font.SysFont("arial",30)

funciones.inicializar(pantalla, font_letra)

font = pygame.font.Font(os.path.join("data","maiden.TTF"),50)
siguiente = menu.menu(pantalla, font)

if not siguiente:
    exit()
# fin de no tocar

# El usuario define su lista de palabras
lista = ["hola", "perro"]

palabra = random.choice(lista)
errores = 0

funciones.definirPalabra(palabra, pygame)

while True:
    pantalla.fill((255, 255, 255))

    letra = funciones.obtenerLetra(pygame)
    if letra == "":
        continue

    if letra in palabra:
        funciones.agregarLetra(letra)
    else:
        errores += 1
        if errores < 11:
            funciones.dibujarAhorcado(errores, pantalla)
        else:
            funciones.dibujarAhorcado(10, pantalla)

    pygame.display.update()
