import funciones
# No tocar 
funciones.inicializar()
# fin de no tocar

# El usuario define su lista de palabras
lista = ["hola", "perro"]

palabra = funciones.elegirPalabra(lista)
errores = 0

ganador = False 

while not ganador and errores < 10:
    funciones.limpiarPantalla()

    letra = funciones.obtenerLetra()
    if errores > 0:
        funciones.dibujarAhorcado(errores)
    
    if letra != "":

        if letra in palabra:
            funciones.agregarLetra(letra)
        else:
            errores += 1

    funciones.mostrarPalabra()

    funciones.actualizar()

    if funciones.validarPalabra():
        ganador = True

funciones.fin(ganador)