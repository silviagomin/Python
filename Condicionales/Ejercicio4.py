#Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.
candidato= input("Elige un candidato (A, B, C): ")

if candidato.upper()=="A":
    print("Ha votado al partido ROJO")
elif candidato.upper()=="B":
    print("Ha votado al partido VERDE")
elif candidato.upper()=="C":
    print("Ha votado al equipo AZUL")
else:
    print("Opción erronea")
