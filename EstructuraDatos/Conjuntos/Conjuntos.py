#Sirven (), {} o []
conjunto={1,2,3,4,5}
print(type(conjunto))

conjunto2=set[(1,2,3,4,5)] #Si no pones el set seria una lista
print(type(conjunto2))

#Metodos conjuntos 
#Dif entre lista y conjunto. No se pueden repetir valores.

conjuntoRepetido={1,1,2,3,3,4,4,5}
listaRepetida=[1,1,2,3,3,4,4,5]
print(conjuntoRepetido) #Elimina los repetidos
print(listaRepetida)


#Añadir datos 
conjuntoAdd={1,2,3,4,5}
print(conjuntoAdd)
conjuntoAdd.add(20)
print(conjuntoAdd)

#Eliminar Datos
#Remove
conjuntoDelete={1,2,3,4,5}
print(conjuntoDelete)
conjuntoDelete.remove(3)
print(conjuntoDelete)
#Discard
conjuntoDelete.discard(1)
print(conjuntoDelete)
#Pop, elimina dato al azar
conjuntoDelete.pop()
print(conjuntoDelete)

#Update. Añade datos.
conjuntoUpdate={1,2,3,4,5,6}
conjuntoUpdate.update([7,8,9])
print(conjuntoUpdate)

#Clear 
conjuntoUpdate.clear()
print(conjuntoUpdate)