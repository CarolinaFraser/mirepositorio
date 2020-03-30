'''
Escribir una funcion sum() y una función multip() que sumen y multipliquen 
respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) 
debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
'''



def suma(lista):
    total = 0
    for i in lista:
        total += i
    return total
print(suma(lista = [1,2,3,4]))


def multip(lista):
    total = 1
    for i in lista:
        total *= i
    return total
print(multip(lista = [1,2,3,4]))

