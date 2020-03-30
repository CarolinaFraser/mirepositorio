'''
Definir una función que calcule la longitud de una lista o una cadena dada. 
(Es cierto que python tiene la función len() incorporada, pero escribirla por 
nosotros mismos resulta un muy buen ejercicio.
'''


def cadena(lista):
    cont = 0
    for i in lista:
        cont = cont + 1
    #print(cont)
    return cont
print(cadena(lista = [1,2,3,4,5,6,7]))

