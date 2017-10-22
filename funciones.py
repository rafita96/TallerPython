import pygame, menu, random, os
from pygame.locals import *

def inicializar():
    pygame.init()

    global font
    global surface
    global font_grande

    surface = pygame.display.set_mode((640,480)) 
    font = pygame.font.SysFont("arial",30)

    font_grande = pygame.font.Font(os.path.join("data","maiden.TTF"),50)

    menu.menu(surface, font_grande)

def elegirPalabra(lista):
    global palabra_secreta
    global palabra_completa

    palabra = random.choice(lista)

    palabra_completa = palabra

    palabra_secreta = "_"*len(palabra)
    surface.fill((255, 255, 255))
    surface.blit(font.render(palabra_secreta,True,(0,0,0)),(250,100))
    pygame.display.update()

    return palabra

def getLetra(e):
    if e.key == K_a:
        return "a"
    elif e.key == K_b:
        return "b"
    elif e.key == K_c:
        return "c"
    elif e.key == K_d:
        return "d"
    elif e.key == K_e:
        return "e"
    elif e.key == K_f:
        return "f"
    elif e.key == K_g:
        return "g"
    elif e.key == K_h:
        return "h"
    elif e.key == K_i:
        return "i"
    elif e.key == K_j:
        return "j"
    elif e.key == K_k:
        return "k"
    elif e.key == K_l:
        return "l"
    elif e.key == K_m:
        return "m"
    elif e.key == K_n:
        return "n"
    elif e.key == K_o:
        return "o"
    elif e.key == K_p:
        return "p"
    elif e.key == K_q:
        return "q"
    elif e.key == K_r:
        return "r"
    elif e.key == K_s:
        return "s"
    elif e.key == K_t:
        return "t"
    elif e.key == K_u:
        return "u"
    elif e.key == K_v:
        return "v"
    elif e.key == K_w:
        return "w"
    elif e.key == K_x:
        return "x"
    elif e.key == K_y:
        return "y"
    elif e.key == K_z:
        return "z"
    else:
        return ""

def limpiarPantalla():
    surface.fill((255, 255, 255))

def obtenerLetra():
    for e in pygame.event.get():
        if e.type == QUIT: 
            exit()
        elif e.type == KEYDOWN:
            letra = getLetra(e)
            return letra
    
    return ""

def validarPalabra():
    global palabra_secreta
    global palabra_completa

    if palabra_completa == palabra_secreta:
        return True
    return False

def agregarLetra(letra):
    global palabra_secreta

    n = len(palabra_completa)
    nueva = []
    for x in palabra_secreta:
        nueva.append(x)

    for i in range(n):
        if palabra_completa[i] == letra:
            nueva[i] = letra

    palabra_secreta = ""
    for x in nueva:
        palabra_secreta = palabra_secreta + x

def mostrarPalabra():
    surface.blit(font.render(palabra_secreta,True,(0,0,0)),(250,100))

def dibujarAhorcado(error):
    """Dibuja cada una de las partes del juego del ahorcado.
       

       Arguments:
       error -- representa las veces que un usuario se equivocó.
       screen -- la pantalla del juego
    """
    
    image = pygame.image.load(os.path.join('data', str(error) + ".jpg"))
    surface.blit(image, (150, 200))

def mostrarPalabraCompleta(var):
    mensaje = "La palabra era: "
    if var:
        mensaje = "La palabra es: "
    surface.blit(font.render(mensaje+palabra_completa,True,(0,0,0)),(200,100))

def fin(ganador):

    perdedor_msg = font_grande.render("HAS PERDIDO!", True, (0, 0, 0))
    ganador_msg = font_grande.render("HAS GANADO!", True, (0, 0, 0))

    while True:
        limpiarPantalla()

        for e in pygame.event.get():
            if e.type == QUIT: 
                exit()

        mostrarPalabraCompleta(ganador)
        
        if ganador:
            surface.blit(ganador_msg, (150, 200))
        else:
            surface.blit(perdedor_msg, (150, 200))

        pygame.display.update()

def actualizar():
    pygame.display.update()