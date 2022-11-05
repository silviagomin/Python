# Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0


def peticion():
    n1= int(input("Introduce un numero: "))
    n2= int(input("Introduce un numero: "))

    if n1 > n2:
        print("{} es mayor que {}" .format(n1, n2))
        return -1

    else:
        print("{} es menor que {}" .format(n1, n2))
        return 0

peticion()