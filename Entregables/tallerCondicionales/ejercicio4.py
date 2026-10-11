# OBJETIVO: Escribir un programa que, dado un número entero, muestre su valor absoluto sin usar la función abs().

# 1. Entrada de datos: pido el número y lo convierto a entero
numero = int(input("Por favor ingresa un número entero: "))

# 2. Condicional para evaluar si el número es negativo
if numero < 0:
    # PROCESO MATEMÁTICO: si es menor a cero, lo multiplico por -1 para volverlo positivo a la fuerza
    valor_absoluto = numero * -1
else:
    # Si es positivo o cero, el valor absoluto es el mismo número, no le hago nada
    valor_absoluto = numero

# 3. Salida en pantalla
print("El valor absoluto es: ", valor_absoluto)
# también pude haber hecho esto: print(f"El valor absoluto es {valor_absoluto}") segun la ia, es mas eficiente y asi lo seguiré haciendo de ahora en adelante.
# Funcionóoooo!!!! <3