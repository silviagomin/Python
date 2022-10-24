numero=3
###########################################
#Seccion Introducción
###########################################
#Dato print
print(numero)

#Type data
print(type(numero))

#multipleVariable in a line 
nombre, apellido ="Silvia", "Gonzalez"

print (nombre)
print(apellido)

###########################################
# Seccion 2 Operaciones aricmeticas
###########################################
print(1+2)
print (18 / 2)

#Operaciones aricmeticas con variables
num1= 5
num2=4

print (num1*num2)

#Ejercicio 1 op aricmetica

print(((3+2)/(2*5))**2)

#Ejercicio 2
payasos=112
munecas=75

print((payasos*23)+(munecas*54))

###########################################
#Seccion 3 Cadenas
###########################################

#Ejercicio 1
cadena="Te quiero solo como amigo"
print( cadena[0:2])

print(cadena[ -3:])
#Imprimir cada 2 caracteres
print(cadena[: :2 ]) #recorre una cadena y haz una copia y recorrela cada 2 caracteres
#Sentido inverso
print(cadena[: :-1] )#Haz una copia e imprime los caracteres y se imprimen a la inversa
#Imprimir en los dos sentidos 
print(cadena + cadena [: : -1])


#Ejercicio2
cadena=" Este es el uso del metodo replace"
print("cadena")
reemplazar=cadena.replace("e", "E")
print(reemplazar)

palabra="Separado"
remplazar=palabra.replace("" , ",")
print(remplazar)