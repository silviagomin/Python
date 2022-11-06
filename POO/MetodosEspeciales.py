class FabricaTelefonos():

    def __init__(self, marca, color): 
        print("Estoy ejecutando el metodo init porque se ah creado un nuevo objeto")
        self.marca= marca
        self.color=color
        print( "el objeto {} ha sido creado".format(self.marca))

    def __str__(self):  
        return "El objeto es {}" . format(self.marca)

    def __del__(self):
        print("El objeto {} ha sido destruido" .format(self.marca))

telefono = FabricaTelefonos("nokia", "negro")
print(telefono.marca)
print(telefono)  #Aqui muestra el espacio en memoria temporal que está utilizando, ademas de llamar a init y a def 
#Si añadimos el metodo str nos muestra un mensaje que le pongamos 
