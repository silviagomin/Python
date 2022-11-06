#Herencia, varias clases y que unas hereden a otras.
#Los metodos de la clase padre pasan a la clase hija sin que sean def de nuevo

class Animales():
    def habla(self):
        print("Yo soy un Animal")

    
class Perro (Animales): #Heredamos de animales, se eredan los metodos y atributos de animales
    pass  #No se coloca nincguna sentencia

animal= Animales()
animal.habla()

perro = Perro()  #perro puede acceder al metodo habla porque o ha heredado
perro.habla()