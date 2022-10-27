#Diccionarios
#Clave es unica en un diccionario
diccionario={'Usuario': "Silvia", 'Contrasena': 1111, }
print(diccionario)

diccionario2={'Nombre':"Silvia", 'Apellido':"Gonzalez", 'Edad': 29}
print(diccionario2.keys()) #Mostrar las claves
print(diccionario2.values()) #Mostrar los valores 

#Valor de una clave
print(diccionario2["Edad"])

#Modificar valor. Adiccion de valor 
diccionario2['Sexo'] = "Mujer"
print(diccionario2)

#Modificar un value del diccionario 
diccionario2["Nombre"]="Maria"
print(diccionario2)

#Metodos de diccionarios ######################################

diccionarioMetodos = {1:2, 2:3, 3:4}
print(diccionarioMetodos)

#Eliminar una clave 
diccionarioMetodos.pop(3)
print(diccionarioMetodos)

#Limpiar todo el diccionario 
#diccionarioMetodos.clear()
#print(diccionarioMetodos)

#Devuelve el valor de la clave 
print(diccionarioMetodos.get(2))

#Añadir un conjunto de clave valor al diccionario 
diccionarioMetodos.setdefault(4,5)
print(diccionarioMetodos)

#Se concatenan los dos diccionarios
diccionarioMetodos2 = {6:7, 8:9}

diccionarioMetodos.update(diccionarioMetodos2)
print(diccionarioMetodos)

#Copy, saca una copia de un diccionario 
diccionarioMetodos.copy()
print(diccionarioMetodos)