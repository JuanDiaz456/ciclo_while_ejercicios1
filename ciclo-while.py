#ejercicio 1

import math 

numero= int(input("digite un numero: "))

while numero<0:
    print("Error -> deberia ser un numero positivo")
    numero= int(input("digite un numero: "))

print(f"\nSu raiz cuadrada es {(math.sqrt(numero)):.2f}")