#Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas

lista = []


def pedirNumeros():
    num = int(input("Cuantos numeros a introducir: "))
    for i in range (num):
        n=int(input("Introduce un numero: "))
        lista.append(n)

def ordenLista():
    lista.sort()
    pares = []
    impares =[]

    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else: 
             impares.append(i)

    print("La lista ordenada de numeros pares: {}" .format(pares))
    print("La lista ordenada de numeros impares: {}" .format(impares))
   

pedirNumeros()
ordenLista()
