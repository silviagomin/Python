# Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras
for i in range (1, 10):
    print(i)

n1= int(input("Introduce el primer numero del rango"))
n2= int(input("Introduce el segundo numero del rango"))

for i in range (n1, n2 +1):
    print (i)