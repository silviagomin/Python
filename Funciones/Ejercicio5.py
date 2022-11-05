#Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio

def areaCuadrado(base, altura):
    area=base*altura
    return area

def areaCirculo (radio):
    area= radio*3.14
    return area


print("El area de un cuadrado es: ", areaCuadrado(2,5))
print("El area de un circulo es: ", areaCirculo(5))