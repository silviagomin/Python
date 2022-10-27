#Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal

letra= (input("Introduce una letra: "))
if letra.lower()=="a":
    print("Es la vocal a")
elif letra.lower()=="e":
    print("Es la vocal e")
elif letra.lower()=="i":
    print("Es la vocal i")
elif letra.lower()=="o":
    print("Es la vocal o")
elif letra.lower()=="u":
    print("Es la vocal u")
else: 
    print("No es una vocal")