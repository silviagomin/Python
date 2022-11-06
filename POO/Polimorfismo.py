#Modificacion de metodos cuando se heredan de otras clases.
#Crear objetos que usen el mismo metodo, pero los objetos sean diferentes.

class Animales():

    def __init__ (self, mensaje):
        self.mensaje=mensaje

    def hablar(self):
        print(self.mensaje)
    
class Perro(Animales):
    #Polimorfismo.
    #Modificacion de un metodo (hablar) heredado de Animales
    def hablar(self):
        print("Yo hago Guuau")

class Pez(Animales):
    #Polimorfismo.
    #Modificacion de un metodo (hablar) heredado de Animales
    def hablar(self):
        print("Yo no hablo")

perro=Perro("Guaoo!")  #No imprime este mensaje porque hemos modificado el metodo hablar dentro de la clase Perro, se va a llamar al metodo modificado y no al heredado
perro.hablar()

animal = Animales("Miau")  #Como lo creo desde la clase animal en vez de Perro muestra Miau
animal.hablar()

pez= Pez("Nada")    #El metodo hablar se está modificando en la clase pez
pez.hablar()