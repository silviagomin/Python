#Init metodo constructor 
#Self forma de equiparar los objetos llamandolos hacia una instancia

class FabricaTelefonos():
    marca="Samsung"


    def CrearHuawei(self):
        self.marca="Huawei"

telefono= FabricaTelefonos()
telefono.CrearHuawei()
print (telefono.marca)


#constructor: primer petodo que se crea en un objeto 
class Fabrica():

    def __init__(self, marca, color): 
        print("Estoy ejecutando el metodo init porque se ah creado un nuevo objeto")
        self.marca= marca
        self.color=color

telefono= Fabrica("nokia","negro")  #El metodo init se llama de manera automatica.
print(telefono.marca)