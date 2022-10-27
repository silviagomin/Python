# if else 
from ast import If

edad=12

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Elif (swich)
#varias condiciones a la vez 
letra="p"

if letra.lower()== "a":
    print("La letra es a")
elif letra.lower()=="e":
    print("La letra es e")
elif letra.lower()=="i":
    print("La letra es i")
elif letra.lower()=="o":
    print("La letra es o")
elif letra.lower()=="u":
    print("La letra es u")
else: 
    print("No es ninguna vocal")

#Condicion anidado
#Condicion dentro de una condicion 
nombre="Silvia"
edad=17

if nombre=="Silvia":
    if edad >= 18:
        print("Eres Silvia y eres mayor de edad")
    else:
        print("Eres Silvia y NO eres mayor de edad")
else: 
    print("No eres Silvia")