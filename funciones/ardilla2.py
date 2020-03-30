'''
Definir una función max_de_tres(), que tome tres números como argumentos y 
devuelva el mayor de ellos.
'''

def maximo(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(str(n1))
    elif n2 > n1 and n2 > n3:
        print(str(n2))
    elif n3 > n1 and n3 > n2:
        print(str(n3))
    else:
        print("son iguales")
        
maximo(3,3,3)