# punto 3: sumar todos los elementos de una lista de forma recursiva

def suma_recursiva(lista):
    """
    Suma todos los numeros dentro de una lista llamandose a si misma elemento por elemento.
    
    Parametros:
        lista (list): Lista con los numeros que queremos sumar.
        
    Retorna:
        int o float: La suma total de todos los elementos de la lista.
    """
    # caso base: si la lista no tiene elementos, la suma es 0
    if len(lista) == 0:
        return 0
    else:
        # caso recursivo: tomamos el primer numero (lista[0]) y le sumamos
        # lo que de la suma del resto de la lista (lista[1:])
        return lista[0] + suma_recursiva(lista[1:])


# --- prueba del punto 3 ---
lista_numeros = [10, 20, 5, 15]
resultado_3 = suma_recursiva(lista_numeros)
print("3. la suma total de", lista_numeros, "es:", resultado_3)