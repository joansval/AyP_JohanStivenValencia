# ordenar una lista con ciclos y luego con función nativa.

# Primero definimos la lista tal cual como la pide el doc
mi_lista = [2, 4, 3, 1, 6, 7, 5, 8, 9, 10]

# Hago una copia exacta de la lista para usarla al final en la comprobación.
# (Si uso la misma, ya va a estar ordenada y no se nota la diferencia)
lista_verificacion = [2, 4, 3, 1, 6, 7, 5, 8, 9, 10]

print(f"Lista original toda desordenada: {mi_lista}\n")


# PARTE 1: ORDENAR LA LISTA (CON CICLOS)

# Nota para mi: la funcion 'len()' significa "length" (longitud), y sirve 
# para contar cuántos elementos hay dentro de la lista. En este caso hay 10.
cantidad = len(mi_lista)

# Vamos a usar dos ciclos 'for' anidados (uno dentro de otro).
# Nota para mi: 'range(cantidad)' crea un rango de números desde 0 hasta la cantidad de elementos.
# Sirve basicamente para decirle al ciclo cuantas vueltas tiene que dar.
for i in range(cantidad):
    
    # El segundo ciclo hace las comparaciones en parejas 
    # El '- i - 1' es un mini truco logico para no comparar los ultimos numeros 
    # que ya se fueron acomodando al final de la lista en las vueltas anteriores.
    for j in range(0, cantidad - i - 1):
        
        # Aqui viene la lógica: si el numero actual es MAYOR que el numero de al lado...
        if mi_lista[j] > mi_lista[j + 1]:
            
            # ... entonces los intercambiamos de lugar!
            # personal: Para cambiar dos variables de lugar sin que se borren,
            # uso una variable 'temporal' (como si fuera un vaso vacio extra para pasar jugo).
            temporal = mi_lista[j]
            mi_lista[j] = mi_lista[j + 1]
            mi_lista[j + 1] = temporal

print(f"Lista ordenada con mis propios ciclos: {mi_lista}")



# PARTE 2: ORDENAR LA LISTA CON LA FUNCION DE PYTHON (COMPROBACION)

# Nota para mi: La funcion '.sort()' es una herramienta predeterminada de Python
# que agarra cualquier lista y la ordena automaticamente de menor a mayor! Es muy importante :D
lista_verificacion.sort()

print(f"Lista ordenada con la funcion de Python: {lista_verificacion}")

#El ciclo lo hicimos perfectoo!!