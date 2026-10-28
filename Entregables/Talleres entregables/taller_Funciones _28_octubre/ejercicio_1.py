# punto 1: calculo del factorial de un numero

def factorial(n):
    """
    Calcula el producto de todos los numeros enteros positivos desde 1 hasta n.
    
    Parametros:
        n (int): Numero entero positivo al que se le va a sacar el factorial.
        
    Retorna:
        int: El resultado de multiplicar 1 * 2 * 3 * ... * n.
    """
    # caso base: cuando llegamos a 1 (o si meten 0), el factorial es 1 y ahi frena la recursion
    if n == 1 or n == 0:
        return 1
    else:
        # caso recursivo: multiplicamos el numero actual 'n' por el factorial del numero anterior (n - 1)
        # por ejemplo: factorial(4) hace 4 * factorial(3), y asi hasta llegar a 1
        return n * factorial(n - 1)


# --- prueba del punto 1 ---
numero = 5
resultado_1 = factorial(numero)
print("1. el factorial de", numero, "es:", resultado_1)