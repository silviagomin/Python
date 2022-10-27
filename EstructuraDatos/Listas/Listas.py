#Listas###################################################
#Colección ordenada de valores mutable
#Sintaxis['Juego', '3', 'coche']

lista = ['Juan', 'Pedro', '3']
print(type(lista))
print(lista[1])
print(len(lista))
##########################################################
#Modificar valor de la lista
lista[1]="Perico"
print (lista)

##########################################################
#Debanado Listas 
lista2=[10,20,3.14,'Silvia', 'Pedro', 'Juan','coche', 3]
print(lista2[3])
print("lista trozos")
print(lista2[0:5])
print(lista2[-1])#Empieza el conteo desde atrás
print(lista2[-5:-2])#Debanado negativo.

##########################################################
#Metodos.
listaMetodos= [1,2,3,4,5]
#Añadir mas datos
print(listaMetodos)
listaMetodos.append(6)
print(listaMetodos)

#Añadir datos en una posicion 
listaMetodos.insert(3, 3.5)
print(listaMetodos)

listaMetodos2=[1,2,3,4,5,2]

#count: Cuantos datos hay en la lista 
print(listaMetodos2.count(2))

#Buscar datos El elemento 4 está en la posicion3
print(listaMetodos2.index(4))
listaOrden=[1,5,6,4,2]
#Ordenar lista
print(listaOrden)
listaOrden.sort() #Orden ascendente
print(listaOrden)
listaOrden.reverse()
print(listaOrden)

##########################################################
#Metodos 3
listaCompleja=['Silvia',24,'Python', 3, 4, 'Coche',' Alex',5]

#Modificar dato en lista compleja
listaCompleja[2]= 'python'
print(listaCompleja)

#Eliminar datos 
print(listaCompleja)
listaCompleja.pop()
print(listaCompleja)

#remove permte parametro
listaCompleja.remove('python')
print(listaCompleja)

####################################################
##Llenar una lista vacia 
listaNumeros1 = [1,2,3]
listaNumeros2 = [4,5,6]

listaNumeros= listaNumeros1 + listaNumeros2
print(listaNumeros)
print("Esta e una lista de datos ", listaNumeros)

listaVacia=[]
print(type(listaVacia))

edad=int(input("Introduce la edad: "))
listaVacia.append(edad)
print(listaVacia)