#Ejercicio 1

#Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

palabra1=input("Introduce una palabra: ")
palabra2= input("Introduce otra palabra:")
if palabra1[-3:] == palabra2[-3:]:
    print("Las palabras riman")
else: 
    print("Las palabras no riman")