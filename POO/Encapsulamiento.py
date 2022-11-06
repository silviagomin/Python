#Aplicar sobre los atributos alcance para que solo pueda ser utilizado dentro de la clase 
class A():
    def __init__(self):
        self.contador=0 

    def incrementar(self):
        self.contador+= 1
    
    def cuenta(self):
        return self.contador
class B():

    #Con los dos __ lo encapsulas. pones en privado el atributo y solo puede ser accedido desde la misma clase 
    def __init__(self):
        self.__contador=0 

    def incrementar(self):
        self.__contador+= 1
    
    def cuenta(self):
        return self.__contador

print("Objeto 1")
a= A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())
#print(a.contador) #Imprime el valor de contador, NO  se debe hacer. NO s eaccede así a los atributos 

print("Objeto2")
b=B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
print(b.__contador)




