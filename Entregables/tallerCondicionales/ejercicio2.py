# OBJETIVO: Pedir dos números al usuario y decir cuál es menor, o si son el mismo número.
# pediré los datos, un número 1 y número 2 entonces 2 variables. Iba a ponerlas de tipo int pero obviamente también deberia de incluir los decimales, entonces lo haré con float
numero_1 = float(input("Ingresa el primer número: "))
numero_2 = float(input("Ingresa el segundo número: "))

# 2. Primera comparación y escenario
if numero_1 < numero_2:
    print("El número menor es el primero que ingresaste =", numero_1)
# 3 probaré el segundo escenario, al contrario
elif numero_2 < numero_1:
    print("El número menor es el segundo que ingresaste =", numero_2)

# 4. Si el primero no es menor, y el segundo tampoco... por pura lógica tienen que ser iguales.
# Aquí ya no necesito evaluar nada más, el else atraparía la única opción que sobra! 
else:
    print("Los dos números son exactamente iguales.")
    
# FIN