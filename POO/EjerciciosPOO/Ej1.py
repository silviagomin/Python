#Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Estudiante ():
    def __init__(self, nombre, nota):
        self.nombre= nombre
        self .nota = nota
       
    def Imprimir(self):
        print("Nombre: {} \nNota: {}" .format(self.nombre, self.nota))

    def Resultado(self):
        if self.nota< 5:
            print("Has suspendido")
        else: 
            print ("Has aprobado")
    
estudiante= Estudiante("SIlvia",10)
estudiante.Imprimir()
estudiante.Resultado()