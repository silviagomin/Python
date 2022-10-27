#Parte 2: Mostrar datos por pantalla:
#Format para mostrar datos por pantalla

nombre= input("Introduce el nombre: ")
edad= int(input("Introduce la edad: "))
print(nombre, edad) #concatenar
#print(nombre+edad) #error diferente tip ode datos 

print("Hola", nombre, "tienes", edad)
print("Hola {} tienes {}".format(nombre, edad))