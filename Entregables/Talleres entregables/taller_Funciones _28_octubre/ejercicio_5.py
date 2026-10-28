# punto 5: encontrar el numero mayor de una lista sin usar max() ni reduce

def encontrar_maximo(lista):
    """
    Busca el numero mas grande dentro de una lista comparando los elementos
    uno por uno de forma recursiva.
    
    Parametros:
        lista (list): Lista de numeros (debe tener al menos un numero).
        
    Retorna:
        int o float: El valor mas grande encontrado en la lista.
    """
    # caso base: si en la lista solo queda 1 elemento, ese mismo es el mayor por defecto
    if len(lista) == 1:
        return lista[0]
    else:
        # paso recursivo: buscamos primero cual es el mayor del resto de la lista (lista[1:])
        mayor_del_resto = encontrar_maximo(lista[1:])
        
        # comparamos uno a uno: el primer numero actual (lista[0]) contra el mayor del resto
        if lista[0] > mayor_del_resto:
            return lista[0]
        else:
            return mayor_del_resto


# --- prueba del punto 5 ---
valores = [14, 85, 23, 99, 42, 7]
resultado_5 = encontrar_maximo(valores)
print("5. de la lista", valores, "el numero mas grande es:", resultado_5)