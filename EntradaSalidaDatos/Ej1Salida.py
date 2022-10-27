#Ejercicio 1

#Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas

vocal=input("Introduce una vocal en minuscula ")
letra= input("Introduce una letra en mayuscula ")

vocal_may= vocal.upper()
letra_may= letra.lower()
print("Vocal: {} Letra: {}" .format(vocal_may,letra_may))