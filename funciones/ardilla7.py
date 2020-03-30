'''
Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas 
invertidas), ejemplo: es_palindromo ("radar") tendría que 
devolver True.
'''

def cadena(frase):
    cadenaInvertida = frase[:: -1]
    if cadenaInvertida == frase:
        return True
    else:
        return False
print(cadena(frase = "ala"))




