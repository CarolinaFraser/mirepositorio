'''
Realiza una función separar(lista) que tome una lista 
de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares y la segunda con los 
números impares.
'''
def separar(numeros):
    pares = []
    impares = []
    for num in numeros:
        if num%2==0:
            pares.append(num)
        else:
            impares.append(num)
    print("Estos son los pares:" + str(pares))
    print("Estos son los impares:" + str(impares))
separar(numeros = [6,5,2,1,7])            