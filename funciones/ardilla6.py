'''
Definir una función inversa() que calcule la inversión 
de una cadena. Por ejemplo la cadena "estoy probando" 
debería devolver la cadena "odnaborp yotse"
'''
def cadena(frase):
    cadenaInvertida = frase[:: -1]
    return cadenaInvertida
print(cadena(frase= "estoy probando"))




