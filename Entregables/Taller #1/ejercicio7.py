# OBJETIVO: Crear un programa que al ingresar un número saque "Fizz" si es múltiplo de 3, 
# "Buzz" si es múltiplo de 5, y "FizzBuzz" si es múltiplo de ambos (3 y 5).

# 1. Pido el número al usuario y de una vez lo convierto a entero (int)
numero = int(input("Ingrese un número entero: "))

# 2. Aquí aplico el operador módulo (%) que ya interioricé en el ejercicio pasado de los años. 
# enonces como necesitamos saber si es múltiplo, el residuo debe dar 0.
# PD: Hace un momento lo intenté al revés (evaluando primero el 3 y el 5 por separado) 
# y vi que no funcionaba porque se saltaba el FizzBuzz.
#Tiene muchísima lógica porque Phyton lee de arriba hacia abajo línea a línea.
# Así que en pocas palabras pues la regla más "importante" o prioritaria tiene que ir de primera:
if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
    
# si no cumplió la doble condición de arriba, entonces ya solo reviso el 3
elif numero % 3 == 0:
    print("Fizz")
    
# si tampoco fue esa, entonces pruebo si es múltiplo de 5
elif numero % 5 == 0:
    print("Buzz")
    
# voy a agregar un ELSE por si el usuario ingresa un número random (tipo 7 o 11) 
# que de plano no sea múltiplo ni de 3 ni de 5
else:
    print(f"El número {numero} no es múltiplo ni de 3 ni de 5")
# FIN