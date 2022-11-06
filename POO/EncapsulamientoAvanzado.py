
class A():
    def __init__(self):
        self._contador = 0    #encapsulamiento el _ avisa al programador que es un atributo encapsulado.
        self._cuenta = 0                   # Solo se debe utilizar dentro de la funcion 

    #metodo get
    @property
    def contador(self):
        return self._contador

    @property   #Ejecutar e metodo como si fuera un atributo
    def cuenta(self):
        return self._cuenta
    
    #metodo Set
    @cuenta.setter
    def cuenta(self, cuenta): #aAdemas del set va el atributo y no hay un return, si no que se cambia el valor 
        self._cuenta= cuenta
        
a = A()
#print(a.cuenta()) #INCORRECTO. No se debe llamar directamente al atributo, está encapsulado. Se utiliza Get  
#a.cuenta=20
#print(a.cuenta)

#Metodo Get: Obtener

#FORMA INCORRECTA de obetener el atributo
#print (a._contador) 
#a._cuenta=10
#print(a.cuenta)

#Forma CORRECTA, llamada a metodo
#print(a.cuenta())

#si añadimos el property, se llama al metodo como atributo 
print(a.cuenta)
print(a.contador)

#Metodo Set Modificar el valor 
#a._cuenta=20 #Incorrecto 
a.cuenta=20 #Se diferencia del get en que hay que modificar el valor primero
print(a.cuenta)