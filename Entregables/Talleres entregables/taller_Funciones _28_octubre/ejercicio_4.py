# punto 4: invertir un texto (string) usando recursividad

def invertir_cadena(texto):
    """
    Recibe una cadena de texto (string) y la devuelve escrita al reves de forma recursiva.
    
    Parametros:
        texto (str): La palabra o frase que se quiere invertir.
        
    Retorna:
        str: El texto completamente invertido.
    """
    # caso base: si el texto esta vacio o le queda una sola letra, se devuelve tal cual
    if len(texto) <= 1:
        return texto
    else:
        # caso recursivo: mandamos a invertir el texto desde la segunda letra en adelante (texto[1:])
        # y al final le pegamos la primera letra (texto[0]) para que vaya quedando de ultima
        return invertir_cadena(texto[1:]) + texto[0]


# --- prueba del punto 4 ---
palabra = "ingenieria"
resultado_4 = invertir_cadena(palabra)
print("4. texto original:", palabra, "-> texto invertido:", resultado_4)