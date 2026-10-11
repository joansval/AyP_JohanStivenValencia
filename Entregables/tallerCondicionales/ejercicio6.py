# OBJETIVO: Solicitar al usuario una letra y, si es una vocal, muestre el mensaje "ES VOCAL"
# Validar que ingrese sólo un carácter; si es más, decir que no se puede procesar el dato.

# 1. A ver... primero pido la letra, y aplico el .lower() que ya conocemos para no preocuparnos con las mayúsculas y minúsculas.
letra = str(input("Por favor ingresa una letra: ").lower())

# 2. Investigué sobre la función len() para contar cuántos caracteres tiene el texto que metió el usuario.
# Sabiendo eso, entonces procedemos: si la longitud es estrictamente mayor a 1, lanzo el mensaje exacto que pide el taller, que era que no se podía
if len(letra) > 1:
    print("No se puede procesar el dato: INGRESE UNA SOLA LETRA :)")

# Si el usuario simplemente le da Enter sin escribir nada (longitud 0), le aviso.
elif len(letra) == 0:
    print("No ingresaste nada, intenta de nuevo.")

else:
    # 3. Si pasó la validación (es exactamente 1 carácter),
    # pasaría con el paso logico 2 que seria ya revisar si es una vocal, entonces:
    # El operador 'in' verifica si esa letra está dentro del texto "aeiou", 
    # esto nos ayuda a ser mas eficients y no tener que escribir un montón de (letra == 'a' or letra == 'e'...) 
    if letra in "aeiou":
        print("es vocal")
    else:
        print("No es vocal (es una consonante o un símbolo)")
# FIN
#FUNCIONÓ!!! No se por que, pero este mini código me encantó!!