'''
Definir una función max() que tome como argumento dos números y devuelva el 
mayor de ellos. (Es cierto que python tiene una función max() incorporada, 
pero hacerla nosotros mismos es un muy buen ejercicio.
'''

def maximo(n1,n2):
    
    if n1 > n2:
        print(str(n1))
    elif n1 < n2:
        print(str(n2))
    else:
        print("Son iguales")

maximo(2,1)