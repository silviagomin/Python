class FabricaTelefonos():

    def __init__(self, marca, *colores,  **modelos):
        self.marca= marca
        self.colores=colores
        self.modelos= modelos 

telefono= FabricaTelefonos("iphone")
print (telefono.marca)

#tupla de colores
telefono = FabricaTelefonos("Iphone", "azul", "negro", "rojo")
print(telefono.colores)

#Diccionario 
telefono = FabricaTelefonos("Iphone", "azul", "negro", m1= "500", m2="X1")
print(telefono.modelos)

#Atributos 
telefono.memoria= 512