#Ejercicio 2
#Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:
#Te llamas: <nombre>
#Tu edad es: <edad>
#Eres: <sexo>

name= input("Introduce el nombre: ")
age= int(input("Introduce tu edad: "))
sex= input("Introduce el sexo:")

print("Te llamas {} \nTu edad es: {} \nEres: {}".format(name, age, sex))