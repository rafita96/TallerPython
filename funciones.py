from pygame.locals import *

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

def obtenerLetra(pygame):
    for e in pygame.event.get():
        if e.type == QUIT: 
            exit()
        elif e.type == KEYDOWN:
            letra = getLetra(e)
            return letra
    
    return ""