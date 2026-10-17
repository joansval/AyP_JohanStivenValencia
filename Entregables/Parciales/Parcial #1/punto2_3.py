# profe para este codigo decidi hacerlo un poquito con comentarios personalizados
# creativos y/o diferentes por asi decir, queria hacerlo mas divertido, perdon por
# comentarios asi jajajaja, me asegure de cumplir al maximo con la rubrica
#  creamos una lista vacia que va a representar la caja de carton donde metemos el arroz
caja = []

# contador para ponerle numero de serie a cada bolsa empacada
numero_bolsa = 1

# variable para mantener la maquina prendida trabajando turno largo
encendida = "si"

print("=== MR. ARROZ' - MAQUINA EMPACADORA AUTOMATICA ===")
print("iniciando turno... cuidado mete la mano en la selladora que no hay seguro medico.")

# ciclo while principal porque la maquina debe trabajar de corrido por largos periodos
while encendida == "si":
    # primero el sensor verifica si hay una bolsa puesta en la boquilla
    # usamos .lower() para pasar a minusculas por si el operario tiene el mayus activado
    hay_bolsa = input("\n[sensor optico] hay una bolsa puesta en la boquilla? (si/no): ").lower()
    
    # rombo del diagrama: verificamos si de verdad hay bolsa antes de soltar el arroz
    if hay_bolsa == "si":
        # paso 1: vaciar el arroz en la bolsa
        print("-> [proceso 1] abriendo compuerta... vaciando 1 kilo de arroz en la bolsa.")
        
        # paso 2: sellar la bolsa cuando ya tiene el arroz adentro
        print("-> [proceso 2] aplicando calor... bolsa sellada al vacio sin regar ni un grano!")
        
        # armamos la etiqueta de la bolsa usando str() para convertir el numero en texto y poder pegarlo
        etiqueta_bolsa = "bolsa_arroz_#" + str(numero_bolsa)
        
        # paso 3: empacar en la caja usando .append() para meter la bolsa al final de nuestra lista
        caja.append(etiqueta_bolsa)
        print("-> [proceso 3] empacada con exito:", etiqueta_bolsa, "Adentro de la caja.")
        
        # mostramos como se va llenando la lista (la caja) en tiempo real
        print("contenido actual de la caja:", caja)
        
        # le sumamos 1 al contador para la proxima bolsa que pase
        numero_bolsa = numero_bolsa + 1
        
    else:
        # si no hay bolsa, bloqueamos la salida de arroz y regañamos al operario
        print("\n[ALERTA ROJA!] jovenazo estas pendejo o que? no ves que no hay bolsa en la boquilla WTF")
        print("menos mal el sensor freno we, si no hacemos un reguero el hpta de arroz aqui por too el piso.")
        print("ponga una bolsa rapido pues mij@, a parte de distrido lent@, coma mr... Mr Arroz :D! Solo pon la bolsa")

    # dejamos esta pregunta afuera del if y del else para que siempre pregunte si la maquina sigue prendida
    encendida = input("\nla maquina sigue encendida operando? (si/no): ").lower()

# cuando apagan la maquina (escriben "no"), cerramos la caja y mostramos el resultado final
print("\n=== FIN DEL TURNO - DESPACHO DE MERCANCIA ===")
print("caja sellada con cinta y lista para subir al camion de distribucion:")
print("contenido final de la caja:", caja)
print("total de bolsas empacadas en este lote:", numero_bolsa - 1)
print("apagando motores... ya se puede ir a preparar su arrocito con huevo.")