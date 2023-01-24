# Programa para simular el abastecimiento de una tienda de Zapatos
# Cada zapato tendrá Talla, estilo y color

import random

print("Aplicación para simular la venta de 100 zapatos\n");
print("Los estilos disponibles son:");

estilos = ["Tenis",
           "Botas",
           "Crocs Metaleras",
           "Mocasines",
           "Sandalia Gladiadora"]

for estilo in estilos:
    print(f"- {estilo}")


print("\nLos Colores Disponibles son:");

colores = ["Verde Selva",
            "Azul Petróleo",
            "Rojo Sangre",
            "Café derrumbe de montaña"
        ]

for color in colores:
    print(f"- {color}")

print("\nLas tallas disponibles son:");

tallas = [ 28, 30, 32, 34, 36, 38, 40, 42, 44 ];

for talla in tallas:
    print(f"- {talla}")

