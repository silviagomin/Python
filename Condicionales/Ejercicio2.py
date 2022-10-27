#Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).

numero=int(input("Introdce un numero entero: "))
valorAbsoluto=0
if numero < 0:
    #valorAbsoluto= (numero*(-1))
    #print("El valor absoluto es {}" .format(valorAbsoluto))
     print ("El valor absoluto es {}" .format (abs(numero)))
elif numero >0: 
    print("El valor absouto es: {}" .format(numero))
else: 
    print("El numero introducido es 0")
