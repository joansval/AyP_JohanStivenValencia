# OBJETIVO: Hacer un programa que permita saber si un año es bisiesto.
# Reglas: Divisible por 4 y no por 100, excepto que también sea divisible por 400.

# 1. Pido el año al usuario y de una vez lo convierto a entero (int)
anio = int(input("Por favor ingresa un año para evaluar (ejemplo: 2024): "))

# 2. Validación de las reglas.
# Explicación de cómo funciona el "modelo":
# 'anio % 4 == 0' -> SÍ es divisible por 4 (el residuo da cero).
# 'and anio % 100 != 0' -> Y al mismo tiempo NO es divisible por 100 (residuo distinto de cero).
# 'or anio % 400 == 0' -> Ó cumple la excepción de ser divisible exacto por 400.

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"¡El año {anio} es bisiesto! Tiene 366 días.")
else:
    print(f"El año {anio} NO es un año bisiesto, es un año 'normal'.")
# FIN