#Ejercicio1
from cmath import sqrt


A= int(input("Introduce el valor de a "))
B= int(input("Introduce el valor de b "))
C= int(input("Introduce el valor de c "))
x1=0
x2=0
print (A)
cont_raiz= ((B**2)-(4*A*B))
if (cont_raiz <0):
    print("No se puede realizar la raiz de un numero negativo")
else:
    x1 = (-B +sqrt((B**2)-(4*A*C)))/(2*A)
    x2 = (-B -sqrt((B**2)-(4*A*C)))/(2*A)

print ("La solucion es: \nx1=",x1, "\nx2=",x2)
