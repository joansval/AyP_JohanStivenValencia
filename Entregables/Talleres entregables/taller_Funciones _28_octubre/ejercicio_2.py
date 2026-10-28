# punto 2: filtrar numeros pares y elevarlos al cuadrado sin usar filter ni map

def pares_al_cuadrado(lista):
    """
    Recorre una lista de numeros de forma recursiva, selecciona unicamente
    los numeros pares y los eleva al cuadrado en un solo paso.
    
    Parametros:
        lista (list): Lista de numeros enteros a procesar.
        
    Retorna:
        list: Nueva lista que contiene solo los numeros pares elevados al cuadrado.
    """
    # caso base: si la lista ya se quedo vacia, devolvemos una lista vacia [] para terminar
    if len(lista) == 0:
        return []
    
    # sacamos el primer numero de la lista en la posicion 0
    primero = lista[0]
    
    # sacamos el resto de la lista (desde la posicion 1 hasta el final) usando [1:]
    resto = lista[1:]
    
    # revisamos si el primer numero es par (el residuo de dividir entre 2 debe ser 0)
    if primero % 2 == 0:
        # si es par, lo elevamos al cuadrado (** 2), lo metemos en una lista y le pegamos el resultado del resto
        return [primero ** 2] + pares_al_cuadrado(resto)
    else:
        # si es impar, lo ignoramos y seguimos revisando solo el resto de la lista
        return pares_al_cuadrado(resto)


# --- prueba del punto 2 ---
numeros_prueba = [1, 2, 3, 4, 5, 6]
resultado_2 = pares_al_cuadrado(numeros_prueba)
print("2. lista original:", numeros_prueba, "-> pares al cuadrado:", resultado_2)