'''
Escribir un programa que le diga al usuario que ingrese una cadena. 
El programa tiene que evaluar la cadena y decir cuantas letras 
mayúsculas tiene.
'''
def c_mayusculas(cadena):
    cont=0
    for i in cadena:
        if i != i.lower():
            cont +=1
    print("La cadena tiene ", cont, "mayusculas")
c_mayusculas("Erase Una vEz en un Puerto")
    
    
  
    


