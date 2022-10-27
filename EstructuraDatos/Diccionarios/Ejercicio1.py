#En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

#{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}


from asyncio.windows_events import NULL
from contextlib import nullcontext


diccionarioPaises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais= input("Introduce un pais: ")

if (diccionarioPaises.get(pais.capitalize())) != None:
    print (diccionarioPaises.get(pais.capitalize()))
else: 
    print("El pais NO esta en la lista")


#Otra forma de resolverlo 

if pais.capitalize() in diccionarioPaises:
    print("La capital del pais es: {} " .format(diccionarioPaises[pais.capitalize()]))
else: 
    print("El pais no está en la lista ")