'''
Escribir una función mas_larga() que tome una lista de 
palabras y devuelva la mas larga.
'''

def mas_larga(lista):
    mas_larga = ""
    for i in lista:
        if len(i) > len(mas_larga):
            mas_larga = i
    return mas_larga
print(mas_larga(lista = ["hermano","primo","tio","sobrino"]))


