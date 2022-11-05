# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
precioFinal=""
precio=""
iva="0"
def factura():
        precio= int(input("Introduce el precio sin IVA: "))
        iva= int(input("IVA  a aplicar: "))
        if iva != 0:
            if iva > 0: 
                precioFinal=precio*iva/100 + precio
                return precioFinal
            else :
                return "El IVA no puede ser negativo"
               
        else: 
           precioFinal=precio*0.21 +precio
           return precioFinal

print("El precio final es", factura())
