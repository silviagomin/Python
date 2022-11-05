while True: 
    try: 
        num1 = int (input("Introduce un numero: "))
        resultado = 100/num1
        print(resultado)
        break
    except ZeroDivisionError:
        print("No se puede dividir entre 0")


while True: 
        try: 
            edad = int(input("Introduce tu edad: "))
            print("Tu edad es ", edad)
            break
        except ValueError:
            print("Valor erroneo")

while True: 
    try:
        edad = int(input("Introduce tu edad: "))
        print("Tu edad es ", edad)
        break
    except KeyboardInterrupt:
            print("\n Has cancelado la eecucion ")
            break