#ejercicio 5
#ejemplo de un menú

num=int(input("menu: 1(ver numeros), 0(salir): "))
while num != 0:
    x=0
    while x<10:
        print("el valor de X es: ",x)
        x+=1
    print("saliendo,,,")
    num=int(input("menu: 1(ver numeros), 0(salir): "))
print("")
print("Gracias")