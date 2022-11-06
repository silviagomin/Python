#Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno

class Fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color= color
        self.precio=precio

class Moto(Fabrica):
    def datos(self):
        print("La cantidad de llantas es de ", self.llantas)
        print("El color de la moto es  ", self.color)
        print("El precio de la moto es  ", self.precio)

class Coche(Fabrica):
    def datos(self):
        print("La cantidad de llantas es de ", self.llantas)
        print("El color del coche  es  ", self.color)
        print("El precio del coche es  ", self.precio)


moto =Moto(2, "Verde", 4000)
moto.datos()

coche=Coche(4, "Azul", 20000)
coche.datos()