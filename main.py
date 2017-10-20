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

while errores < 10:
    pantalla.fill((255, 255, 255))

    letra = funciones.obtenerLetra(pygame)
    if errores > 0:
        funciones.dibujarAhorcado(errores, pantalla)
    
    if letra != "":

        if letra in palabra:
            funciones.agregarLetra(letra)
        else:
            errores += 1

    funciones.mostrarPalabra()
        

    pygame.display.update()



loser = font.render("HAS PERDIDO!", True, (0, 0, 0))
while True:
    pantalla.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == QUIT: 
            exit()
    pantalla.blit(loser, (80, 240))
    pygame.display.update()