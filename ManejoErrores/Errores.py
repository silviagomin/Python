#Ejemplo Si en un int el usuario escribe un string 
#edad= int(input("Introduce tu edad: "))
#18
# print("La edad es ", edad)

while True:
    try: 
        edad= int(input("Introduce tu edad: "))
        print("La edad es ", edad)
    except:
        print("Ingresaste un valor erroneo")