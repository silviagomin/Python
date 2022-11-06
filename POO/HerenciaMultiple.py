class A():
    def primera(self):
        return "Esta es la clase A"
    
class B():
    def segunda(Self):
        return ("Esta es la clase B")


#Mas de una clase son heredadas a otra
#C es hija de A y de B.
#La clase A y B son padres de la C
class C (A, B):
    pass

#C hereda los metodos de A y B
c= C()
print(c.primera())
print(c.segunda())