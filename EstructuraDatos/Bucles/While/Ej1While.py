#Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero
i=0
numero=int(input("Introduce un numero"))
print("La tabla de multiplicar del numero {}".format(numero))

while i <= 10: 
    print("{} x {} = {} " .format(numero, i, numero*i))
    i+=1
