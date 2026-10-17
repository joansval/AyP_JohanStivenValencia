# variable para ir sumando toda la plata que va a pagar el grupo familiar en total
total_grupo = 0

# variable para controlar el ciclo while, la iniciamos en "si" para que arranque la primera vez
otro = "si"

print("=== MAQUINA DE COBROS: SALA DE JUEGOS ===")
print("bienvenidos! vamos a ver cuanta plata nos van a dejar hoy en las maquinitas.")

# usamos un ciclo while para poder registrar a varias personas de la misma familia sin que se cierre
while otro == "si":
    # pedimos la edad y usamos int() para convertir el texto que entra en un numero entero
    # esto es super importante porque si no, python lo lee como letras y no podemos usar los simbolos < o >
    edad = int(input("\npor favor, ingrese la edad del cliente (sin quitarse años): "))
    
    # primer rombo del diagrama: comprobamos si tiene menos de 5 años
    if edad < 5:
        precio = 0
        print("ahhh tan lindo el bebe. como tiene menos de 5 añitos, entra totalmente gratis! valor: $0")
        
    # segundo rombo: si tiene entre 5 y 18 años (incluyendo el 18, por eso usamos <=)
    # usamos 'and' para obligar a que se cumplan las dos condiciones a la vez
    elif edad >= 5 and edad <= 18:
        precio = 5
        print("tarifa juvenil aplicada. ya esta grande pero todavia lo mantienen en la casa. paga: $5")
        
    # por descarte (else), si no es menor de 5, ni menor o igual a 18, es porque es adulto
    else:
        precio = 10
        print("tarifa de adulto. usted ya deberia estar pagando impuestos y deudas. paga: $10")
        
    # a la variable total_grupo le sumamos el precio de la entrada que acabamos de calcular
    total_grupo = total_grupo + precio
    
    # preguntamos si viene mas gente en el grupo
    # usamos .lower() para pasar la respuesta a minusculas por si el usuario escribe "SI" en mayusculas
    otro = input("va a meter a otro familiar a la sala de juegos? (si/no): ").lower()

# cuando ya no quieran meter a nadie mas y escriban "no", mostramos cuanto es el cobro final
print("\n=== RESUMEN DEL ROBO... DIGO, DE TAQUILLA ===")
print("el total a pagar por toda la familia es de: $", total_grupo)
print("gracias por venir, vuelva pronto y no se gaste todo el sueldo en los juegos!")