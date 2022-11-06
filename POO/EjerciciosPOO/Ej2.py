# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora():
    def __init__(self):
        self.num1 = int(input("Introduce numero1: "))
        self.num2 = int(input("Introduce numero2: "))

    def suma(self):
        self.suma= self.num1 + self.num2
        return "La suma es:", self.suma

    def resta (self):
        self.resta= self.num1- self.num2
        return "La resta es: ", self.resta

    def multiplicacion(self):
        self.multiplicacion= self.num1* self.num2
        return "La multiplicacion es: ", self.multiplicacion
    
    def division (self):
        if (self.num2 !=0):
            self.division= self.num1/self.num2
            return "La division es: ",self.division 
        else: 
            return "No se puede dvidir entre 0 "
            


calculadora=Calculadora()
print(calculadora.suma())
print(calculadora.resta())
print(calculadora.multiplicacion())
print(calculadora.division())
