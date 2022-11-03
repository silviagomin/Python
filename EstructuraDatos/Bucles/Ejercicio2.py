#Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares

n1= int(input("Introduce el primer numero del rango"))
n2= int(input("Introduce el segundo numero del rango"))

for i in range (n1, n2):
    if ( (i % 2) ==0 ):
        continue
    print (i)