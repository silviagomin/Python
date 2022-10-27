#En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:
#[20, 50, "Curso", 'Python', 3.14]
lista=[20,50,"Curso", "Python", 3.14]
print(lista)
cambio1=input("Introduce un nuevo valor para la primera posicion: ")
cambio2= input("Introduce un nuevo valor para la segunda posicion: ")

lista[0]=cambio1
lista[1]=cambio2

print("La nueva lista es: ", lista)