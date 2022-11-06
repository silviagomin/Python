# Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.

class Universidad():
    def __init__(self, nombreUniversidad):
        self.nombreUniversidad=nombreUniversidad
        
class Carrera():
    def carrera(self, carrera):
        self.carrera=carrera
       
class Estudiante(Universidad, Carrera):   
    def datos(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        print("Nombre: {}\nEdad: {} \nEspecialidad: {} \nUniversidad: {}".format(self.nombre, self.edad, self.carrera, self.nombreUniversidad))


persona= Estudiante("Universidad de Salamanca")
persona.carrera("Ingenieria Informática")
persona.datos("Silvia", 28)