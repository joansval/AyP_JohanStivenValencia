# Nota para mi: Como el profe dice que pueden ser "uno o varios pedidos", 
# tengo que usar un ciclo para repetir el menu y sumar los precios.
# Voy a usar el ciclo 'while' (mientras que).

print("¡Bienvenido a Heladería Helados Fríos! Donde el servicio es tan frío como nuestros helados.")

# Creo una variable en 0 para ir sumando la cuenta de todos los helados que pida.
total_a_pagar = 0.0 

# Creo esta variable como un "interruptor" para que el ciclo pueda arrancar.
# Le pongo "si" por defecto para que entre al ciclo al menos la primera vez.
comprar_mas = "si".lower()

# AQUI ARRANCA EL CICLO
# Esto se lee: "mientras que la variable comprar_mas sea igual a 'si', repita todo lo de abajo"
while comprar_mas == "si" or comprar_mas == "sí":
    # \n para salto de línea (espacio)
    print("\n--- MENÚ DE HELADOS ---")
    print("El helado base (puro y triste) cuesta $1.90")
    print("Opciones de topping (solo puede elegir uno, no se emocione):")
    print("1. Sin topping (+$0.00)")
    print("2. Topping de Frutas (+$0.50)")
    print("3. Topping de Granola (+$1.50)")
    print("4. Topping de Oreo (+$1.00)")
    print("5. Topping de Brownie (+$0.75)")
    
    # Pido el topping. tambien puede hacerlo por numero.
    # El .lower() pasa todo a minusculas y el .strip() borra espacios accidentales, 
    # asi evitamos errores si el usuario escribe raro.
    topping_elegido = input("\nEscriba el nombre o el NÚMERO del topping que desea (ej. 'oreo', '4' o 'sin topping'): ").lower().strip()
    
    # El helado base siempre vale 1.90, sin importar el topping
    precio_helado = 1.90
    
    # Empiezo a evaluar el topping que escribio con los condicionales que ya conozco.
    # Nota para mi: Evaluo el numero entre comillas (ej: "1") para que python lo lea como texto.
    if topping_elegido == "sin topping" or topping_elegido == "sin" or topping_elegido == "1":
        precio_helado = 1.90
        # 2f nos indica los decimales demás a mostrar
        print(f"Helado sencillo. Qué básico, aburrido y pobre eres. Te cuesta: ${precio_helado:.2f}")
        
    elif topping_elegido == "frutas" or topping_elegido == "fruta" or topping_elegido == "2":
        precio_helado = 1.90 + 0.50
        print(f"Ah, intentando ser fitness comiendo helado... Ok. Su helado con frutas cuesta: ${precio_helado:.2f}")
        
    elif topping_elegido == "granola" or topping_elegido == "3":
        precio_helado = 1.90 + 1.50
        print(f"Helado con alpiste, digo, granola. Para estropear el paladar. Son: ${precio_helado:.2f}")
        
    elif topping_elegido == "oreo" or topping_elegido == "4":
        precio_helado = 1.90 + 1.00
        print(f"El clásico de los indecisos. Su helado con Oreo cuesta: ${precio_helado:.2f}")
        
    elif topping_elegido == "brownie" or topping_elegido == "5":
        precio_helado = 1.90 + 0.75
        print(f"Alguien quiere un coma diabético hoy. Excelente elección. Son: ${precio_helado:.2f}")
        
    else:
        # Si ponen un topping random que no existe o un numero raro, cae aqui
        print(f"¿Acaso viste '{topping_elegido}' en el menú? No tenemos eso aquí.")
        print(f"Le daremos el helado sencillo sin topping por: ${precio_helado:.2f}. Agradezca que le damos algo.")
        precio_helado = 1.90
    
    # PROCESO MATEMATICO: Ahora sumo el costo de ESTE helado al total de la cuenta
    total_a_pagar = total_a_pagar + precio_helado
    
    # Le pregunto si quiere otro helado. Dependiendo de lo que responda, 
    # el 'while' vuelve a dar otra vuelta, o se rompe y termina el ciclo.
    comprar_mas = input("\n¿Va a querer otro helado o ya se va? (si/no): ").lower().strip()

# ESTA PARTE YA ESTA FUERA DEL CICLO (no tiene sangria a la izquierda).
# Solo se ejecuta cuando el usuario dice que "no" quiere mas y el 'while' se acaba.

print("\n" + "="*40) # Esto es solo para imprimir una linea separadora y que se vea bonito Y ponga 40 =
# Nota para mi: ese :.2f dentro de las llaves es para que el numero salga 
# con dos decimales exactos siempre (ej: $2.40 en vez de $2.4).
print(f"Tanto tiempo pa tan poco we, NO JODÁS!!. El total a pagar por sus helados es de: ${total_a_pagar:.2f}. Pase a la caja.")
print("="*40)