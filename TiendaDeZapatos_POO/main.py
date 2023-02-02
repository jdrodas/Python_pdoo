# Programa para simular el abastecimiento de una tienda de Zapatos
# Cada zapato tendrá Talla, estilo y color

import random

print("Aplicación para simular la venta de zapatos\n")

#Aqui pedimos cuantos zapatos tendrá la tienda
datoCorrecto = False
cantidad = 0

while (datoCorrecto == False):
    datoCantidad = input("\nIngresa la cantidad de zapatos que tendrá la tienda: ")

    if datoCantidad.isdigit():
        cantidad = int(datoCantidad)
        if(cantidad>0):
            datoCorrecto = True
        else:
            print("El dato ingresado no representa una cantidad válida. Intenta nuevamente!")
    else:
        print("El dato ingresado no está en el formato correcto. Intenta nuevamente!")


print(f"\nSe abastecerá la tienda con {cantidad} zapatos")


print("\nLos estilos disponibles son:")

estilos = ["Tenis",
           "Botas",
           "Crocs Metaleras",
           "Mocasines",
           "Sandalia Gladiadora"]

for estilo in estilos:
    print(f"- {estilo}")


print("\nLos Colores Disponibles son:")

colores = ["Verde Selva",
            "Azul Petróleo",
            "Rojo Sangre",
            "Café derrumbe de montaña"
        ]

for color in colores:
    print(f"- {color}")

print("\nLas tallas disponibles son:")

tallas = [28, 30, 32, 34, 36, 38, 40, 42, 44]

for talla in tallas:
    print(f"- {talla}")

print("\nLa tienda quedó surtida con estos zapatos:")

